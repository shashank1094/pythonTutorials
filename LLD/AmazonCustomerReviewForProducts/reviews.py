from datetime import datetime
from typing import List, Dict
import uuid


class User:
    def __init__(self, name: str, email: str):
        self.user_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.reviews = []  # List of review IDs

    def __repr__(self):
        return f"User({self.name}, {self.email})"


class Product:
    def __init__(self, name: str, category: str, description: str, price: float):
        self.product_id = str(uuid.uuid4())
        self.name = name
        self.category = category
        self.description = description
        self.price = price
        self.reviews = []  # List of Review IDs

    def __repr__(self):
        return f"Product({self.name}, {self.category}, ${self.price})"


class Review:
    def __init__(self, user: User, product: Product, rating: int, text: str, media: List[str] = []):
        self.review_id = str(uuid.uuid4())
        self.user = user
        self.product = product
        self.rating = rating  # 1-5 stars
        self.text = text
        self.media = media  # Image/Video URLs
        self.timestamp = datetime.now()
        self.upvotes = 0
        self.downvotes = 0
        self.comments = []  # List of Comment IDs

        # Link review to user and product
        user.reviews.append(self.review_id)
        product.reviews.append(self.review_id)

    def upvote(self):
        self.upvotes += 1

    def downvote(self):
        self.downvotes += 1

    def add_comment(self, comment):
        self.comments.append(comment.comment_id)

    def __repr__(self):
        return f"Review({self.user.name}, {self.product.name}, {self.rating}⭐)"


class Comment:
    def __init__(self, user: User, review: Review, text: str):
        self.comment_id = str(uuid.uuid4())
        self.user = user
        self.review = review
        self.text = text
        self.timestamp = datetime.now()

        # Link comment to review
        review.add_comment(self)

    def __repr__(self):
        return f"Comment({self.user.name}, {self.text})"


class ReviewSystem:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.products: Dict[str, Product] = {}
        self.reviews: Dict[str, Review] = {}
        self.comments: Dict[str, Comment] = {}

    def add_user(self, name: str, email: str) -> User:
        user = User(name, email)
        self.users[user.user_id] = user
        return user

    def add_product(self, name: str, category: str, description: str, price: float) -> Product:
        product = Product(name, category, description, price)
        self.products[product.product_id] = product
        return product

    def add_review(self, user: User, product: Product, rating: int, text: str, media: List[str] = []) -> Review:
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")

        review = Review(user, product, rating, text, media)
        self.reviews[review.review_id] = review
        return review

    def add_comment(self, user: User, review: Review, text: str) -> Comment:
        comment = Comment(user, review, text)
        self.comments[comment.comment_id] = comment
        return comment

    def get_product_reviews(self, product: Product, sort_by="recent") -> List[Review]:
        reviews = [self.reviews[rev_id] for rev_id in product.reviews]

        if sort_by == "rating":
            return sorted(reviews, key=lambda r: r.rating, reverse=True)
        elif sort_by == "helpfulness":
            return sorted(reviews, key=lambda r: (r.upvotes - r.downvotes), reverse=True)
        return sorted(reviews, key=lambda r: r.timestamp, reverse=True)

    def moderate_review(self, admin, review: Review):
        """Admins can remove inappropriate reviews"""
        if isinstance(admin, Admin):
            del self.reviews[review.review_id]
            review.user.reviews.remove(review.review_id)
            review.product.reviews.remove(review.review_id)


class Admin(User):
    def __init__(self, name: str, email: str):
        super().__init__(name, email)

    def remove_review(self, review_system: ReviewSystem, review: Review):
        review_system.moderate_review(self, review)


if __name__ == "__main__":
    review_system = ReviewSystem()

    # Create Users
    user1 = review_system.add_user("Alice", "alice@example.com")
    user2 = review_system.add_user("Bob", "bob@example.com")

    # Create Product
    product = review_system.add_product("Laptop X", "Electronics", "High-performance laptop", 999.99)

    # Add Reviews
    review1 = review_system.add_review(user1, product, 5, "Great product!", ["image1.jpg"])
    review2 = review_system.add_review(user2, product, 4, "Good but expensive.")

    # Add Comments
    comment1 = review_system.add_comment(user2, review1, "I agree, it's awesome!")

    # Upvote Review
    review1.upvote()
    review1.upvote()
    review2.downvote()

    # Fetch and Sort Reviews
    print("Recent Reviews:", review_system.get_product_reviews(product, sort_by="recent"))
    print("Highest Rated Reviews:", review_system.get_product_reviews(product, sort_by="rating"))

    # Admin Moderation
    admin = Admin("AdminUser", "admin@example.com")
    admin.remove_review(review_system, review2)

    print("Reviews after moderation:", review_system.get_product_reviews(product, sort_by="recent"))
