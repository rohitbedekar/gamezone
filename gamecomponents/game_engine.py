class GameEngine:
    def get_divisors(self, num):
        divisors = {}
        counter = 1
        for i in range(2, num):
            if num % i == 0:
                divisors[counter] = i
                counter += 1

        return divisors

    def is_prime(self, divisors):
        return len(divisors) == 0
