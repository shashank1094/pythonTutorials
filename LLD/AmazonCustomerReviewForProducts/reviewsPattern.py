import uuid
from datetime import datetime
from abc import ABC, abstractmethod

# ===== Singleton Pattern (Ensures only one ReviewSystem exists) =====
class ReviewSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ReviewSystem, cls).__new__(cls)
            cls._instance.users = {}
            cls._instance.products = {}
            cls._instance.reviews = {}
            cls._instance.comments = {}
        return cls._instance

    def add_user(self, name: str, email: str):
        user = UserFactory.create_user(name, email)
        self.users[user.user_id] = user
        return user

    def add_product(self, name: str, category: str, description: str, price: float):
        product = ProductFactory.create_product(name, category, description, price)
        self.products[product.product_id] = product
        return product

    def add_review(self, user, product, rating, text, media=None):
        if not media:
            media = []
        review = ReviewFactory.create_review(user, product, rating, text, media)
        self.reviews[review.review_id] = review
        return review

    def get_reviews(self, product, sort_strategy):
        return sort_strategy.sort(self.reviews, product)

# ===== Factory Pattern (Creates Objects) =====
class UserFactory:
    @staticmethod
    def create_user(name, email):
        return User(name, email)

class ProductFactory:
    @staticmethod
    def create_product(name, category, description, price):
        return Product(name, category, description, price)

class ReviewFactory:
    @staticmethod
    def create_review(user, product, rating, text, media):
        return Review(user, product, rating, text, media)

# ===== Observer Pattern (Notifying Users of Upvotes and Comments) =====
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class User(Observer):
    def __init__(self, name, email):
        self.user_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.notifications = []

    def update(self, message):
        self.notifications.append(message)
        print(f"Notification for {self.name}: {message}")

class Product:
    def __init__(self, name, category, description, price):
        self.product_id = str(uuid.uuid4())
        self.name = name
        self.category = category
        self.description = description
        self.price = price
        self.reviews = []

class Review:
    def __init__(self, user, product, rating, text, media):
        self.review_id = str(uuid.uuid4())
        self.user = user
        self.product = product
        self.rating = rating
        self.text = text
        self.media = media
        self.timestamp = datetime.now()
        self.upvotes = 0
        self.downvotes = 0
        self.comments = []
        self.observers = [user]  # The user is subscribed to notifications

        # Link the review to the product
        product.reviews.append(self)

    def upvote(self):
        self.upvotes += 1
        self.notify_observers(f"Your review for {self.product.name} got an upvote!")

    def downvote(self):
        self.downvotes += 1

    def add_comment(self, comment):
        self.comments.append(comment)
        self.notify_observers(f"Your review for {self.product.name} got a new comment!")

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

class Comment:
    def __init__(self, user, review, text):
        self.comment_id = str(uuid.uuid4())
        self.user = user
        self.review = review
        self.text = text
        self.timestamp = datetime.now()
        review.add_comment(self)

# ===== Decorator Pattern (Moderation System) =====
class ReviewModerator:
    def __init__(self, review):
        self.review = review

    def moderate(self):
        banned_words = ["bad", "fake"]
        for word in banned_words:
            if word in self.review.text.lower():
                print(f"Review {self.review.review_id} contains inappropriate content and is removed.")
                return None
        return self.review

# ===== Strategy Pattern (Sorting Strategies for Reviews) =====
class ReviewSortStrategy(ABC):
    @abstractmethod
    def sort(self, reviews, product):
        pass

class SortByRecent(ReviewSortStrategy):
    def sort(self, reviews, product):
        product_reviews = [reviews[review_id] for review_id in product.reviews]
        return sorted(product_reviews, key=lambda r: r.timestamp, reverse=True)

class SortByRating(ReviewSortStrategy):
    def sort(self, reviews, product):
        product_reviews = [reviews[review_id] for review_id in product.reviews]
        return sorted(product_reviews, key=lambda r: r.rating, reverse=True)

class SortByHelpfulness(ReviewSortStrategy):
    def sort(self, reviews, product):
        product_reviews = [reviews[review_id] for review_id in product.reviews]
        return sorted(product_reviews, key=lambda r: r.upvotes - r.downvotes, reverse=True)

# ===== Example Usage =====
if __name__ == "__main__":
    review_system = ReviewSystem()

    # Create Users
    user1 = review_system.add_user("Alice", "alice@example.com")
    user2 = review_system.add_user("Bob", "bob@example.com")

    # Create Product
    product = review_system.add_product("Laptop X", "Electronics", "High-performance laptop", 999.99)

    # Add Reviews
    review1 = review_system.add_review(user1, product, 5, "Amazing laptop!", ["image1.jpg"])
    review2 = review_system.add_review(user2, product, 3, "Bad quality screen...")

    # Moderate a review
    moderated_review = ReviewModerator(review2).moderate()
    if moderated_review:
        print("Review Approved:", moderated_review.text)

    # Add Comments
    comment1 = Comment(user2, review1, "I agree, it's awesome!")

    # Upvote Review
    review1.upvote()
    review1.upvote()
    review2.downvote()

    # Fetch Sorted Reviews
    print("Recent Reviews:", review_system.get_reviews(product, SortByRecent()))
    print("Highest Rated Reviews:", review_system.get_reviews(product, SortByRating()))
