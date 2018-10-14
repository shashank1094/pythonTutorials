class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, s, t):
        freq_t = {}
        freq_s = {}
        for item in set(t):
            freq_t[item] = t.count(item)
            freq_s[item] = s.count(item)
            if freq_t[item] > freq_s[item]:
                return ''
        # print(freq_s, freq_t, sep='\n\n\n')
        start, end = 0, len(s) - 1
        start_done, end_done = False, False
        while start <= end and not (start_done and end_done):
            print(freq_s, freq_t, s[start], s[end], sep='\n\n\n', end='\n^^^\n')
            if not start_done:
                if s[start] in freq_s:
                    if freq_s[s[start]] > freq_t[s[start]]:
                        freq_s[s[start]] -= 1
                        start += 1
                    else:
                        start_done = True
                else:
                    start += 1
            else:
                if s[end] in freq_s:
                    if freq_s[s[end]] > freq_t[s[end]]:
                        freq_s[s[end]] -= 1
                        end -= 1
                    else:
                        end_done = True
                else:
                    end -= 1

        return s[start: end + 1]


if __name__ == '__main__':
    sol1 = Solution()
    print(sol1.minWindow("xiEjBOGeHIMIlslpQIZ6jERaAVoHUc9Hrjlv7pQpUSY8oHqXoQYWWll8Pumov89wXDe0Qx6bEjsNJQAQ0A6K21Z0BrmM96FWEdRG69M9CYtdBOrDjzVGPf83UdP3kc4gK0uHVKcPN4HPdccm9Qd2VfmmOwYCYeva6BSG6NGqTt1aQw9BbkNsgAjvYzkVJPOYCnz7U4hBeGpcJkrnlTgNIGnluj6L6zPqKo5Ui75tC0jMojhEAlyFqDs7WMCG3dmSyVoan5tXI5uq1IxhAYZvRQVHtuHae0xxwCbRh6S7fCLKfXeSFITfKHnLdT65K36vGC7qOEyyT0Sm3Gwl2iXYSN2ELIoITfGW888GXaUNebAr3fnkuR6VwjcsPTldQSiohMkkps0MH1cBedtaKNoFm5HbH15kKok6aYEVsb6wOH2w096OwEyvtDBTQwoLN87JriLwgCBBavbOAiLwkGGySk8nO8dLHuUhk9q7f0rIjXCsQeAZ1dfFHvVLupPYekXzxtWHd84dARvv4Z5L1Z6j8ur2IXWWbum8lCi7aErEcq41WTo8dRlRykyLRSQxVH70rUTz81oJS3OuZwpI1ifBAmNXoTfznG2MXkLtFu4SMYC0bPHNctW7g5kZRwjSBKnGihTY6BQYItRwLUINApd1qZ8W4yVG9tnjx4WyKcDhK7Ieih7yNl68Qb4nXoQl079Vza3SZoKeWphKef1PedfQ6Hw2rv3DpfmtSkulxpSkd9ee8uTyTvyFlh9G1Xh8tNF8viKgsiuCZgLKva32fNfkvW7TJC654Wmz7tPMIske3RXgBdpPJd5BPpMpPGymdfIw53hnYBNg8NdWAImY3otYHjbl1rqiNQSHVPMbDDvDpwy01sKpEkcZ7R4SLCazPClvrx5oDyYolubdYKcvqtlcyks3UWm2z7kh4SHeiCPKerh83bX0m5xevbTqM2cXC9WxJLrS8q7XF1nh", "dO4BRDaT1wd0YBhH88Afu7CI4fwAyXM8pGoGNsO1n8MFMRB7qugS9EPhCauVzj7h"))
