import unittest
import solution


class TestWesternSigns(unittest.TestCase):

    def test_taurus_signs(self):
        self.assertEqual(solution.interpret_western_sign(1, 5), 'taurus')

    def test_capricorn(self):
        self.assertEqual(solution.interpret_western_sign(23, 12), 'capricorn')

    def test_gemini(self):
        self.assertEqual(solution.interpret_western_sign(18, 6), 'gemini')

    def test_cancer(self):
        self.assertEqual(solution.interpret_western_sign(19, 7), 'cancer')


class TestChineseSigns(unittest.TestCase):

    def test_tiger_sign(self):
        self.assertEqual(solution.interpret_chinese_sign(1986), 'tiger')

    def test_dragon_sign(self):
        self.assertEqual(solution.interpret_chinese_sign(2000), 'dragon')

    def test_dog_sign(self):
        self.assertEqual(solution.interpret_chinese_sign(1994), 'dog')

    def test_monkey_sign(self):
        self.assertEqual(solution.interpret_chinese_sign(1992), 'monkey')


class TestBothSigns(unittest.TestCase):

    def test_aries_snake_signs(self):
        self.assertEqual(
            solution.interpret_both_signs(18, 4, 1989),
            ('aries', 'snake')
        )

    def test_aquarius_pig(self):
        self.assertEqual(
            solution.interpret_both_signs(23, 1, 2007),
            ('aquarius', 'pig')
        )

    def test_leo_rat(self):
        self.assertEqual(
            solution.interpret_both_signs(26, 7, 1936),
            ('leo', 'rat')
        )


class TestSigns(unittest.TestCase):

    def test_western_signs_aquarius(self):
        self.assertEqual(solution.interpret_western_sign(21, 1), 'aquarius')
        self.assertEqual(solution.interpret_western_sign(18, 2), 'aquarius')
        self.assertNotEqual(solution.interpret_western_sign(20, 1), 'aquarius')
        self.assertNotEqual(solution.interpret_western_sign(21, 2), 'aquarius')

    def test_western_signs_pisces(self):
        self.assertEqual(solution.interpret_western_sign(19, 2), 'pisces')
        self.assertEqual(solution.interpret_western_sign(20, 3), 'pisces')
        self.assertNotEqual(solution.interpret_western_sign(18, 2), 'pisces')
        self.assertNotEqual(solution.interpret_western_sign(21, 3), 'pisces')

    def test_western_signs_aries(self):
        self.assertEqual(solution.interpret_western_sign(21, 3), 'aries')
        self.assertEqual(solution.interpret_western_sign(20, 4), 'aries')
        self.assertNotEqual(solution.interpret_western_sign(20, 3), 'aries')
        self.assertNotEqual(solution.interpret_western_sign(21, 4), 'aries')

    def test_western_signs_taurus(self):
        self.assertEqual(solution.interpret_western_sign(21, 4), 'taurus')
        self.assertEqual(solution.interpret_western_sign(20, 5), 'taurus')
        self.assertNotEqual(solution.interpret_western_sign(20, 4), 'taurus')
        self.assertNotEqual(solution.interpret_western_sign(21, 5), 'taurus')

    def test_western_signs_gemini(self):
        self.assertEqual(solution.interpret_western_sign(21, 5), 'gemini')
        self.assertEqual(solution.interpret_western_sign(20, 6), 'gemini')
        self.assertNotEqual(solution.interpret_western_sign(20, 5), 'gemini')
        self.assertNotEqual(solution.interpret_western_sign(21, 6), 'gemini')

    def test_western_signs_cancer(self):
        self.assertEqual(solution.interpret_western_sign(21, 6), 'cancer')
        self.assertEqual(solution.interpret_western_sign(22, 7), 'cancer')
        self.assertNotEqual(solution.interpret_western_sign(20, 6), 'cancer')
        self.assertNotEqual(solution.interpret_western_sign(23, 7), 'cancer')

    def test_western_signs_leo(self):
        self.assertEqual(solution.interpret_western_sign(23, 7), 'leo')
        self.assertEqual(solution.interpret_western_sign(22, 8), 'leo')
        self.assertNotEqual(solution.interpret_western_sign(22, 7), 'leo')
        self.assertNotEqual(solution.interpret_western_sign(23, 8), 'leo')

    def test_western_signs_virgo(self):
        self.assertEqual(solution.interpret_western_sign(23, 8), 'virgo')
        self.assertEqual(solution.interpret_western_sign(22, 9), 'virgo')
        self.assertNotEqual(solution.interpret_western_sign(22, 8), 'virgo')
        self.assertNotEqual(solution.interpret_western_sign(23, 9), 'virgo')

    def test_western_signs_libra(self):
        self.assertEqual(solution.interpret_western_sign(23, 9), 'libra')
        self.assertEqual(solution.interpret_western_sign(22, 10), 'libra')
        self.assertNotEqual(solution.interpret_western_sign(22, 9), 'libra')
        self.assertNotEqual(solution.interpret_western_sign(23, 10), 'libra')

    def test_western_signs_scorpio(self):
        self.assertEqual(solution.interpret_western_sign(23, 10), 'scorpio')
        self.assertEqual(solution.interpret_western_sign(21, 11), 'scorpio')
        self.assertNotEqual(solution.interpret_western_sign(22, 10), 'scorpio')
        self.assertNotEqual(solution.interpret_western_sign(22, 11), 'scorpio')

    def test_western_signs_sagittarius(self):
        self.assertEqual(solution.interpret_western_sign(22, 11), 'sagittarius')
        self.assertEqual(solution.interpret_western_sign(21, 12), 'sagittarius')
        self.assertNotEqual(solution.interpret_western_sign(21, 11), 'sagittarius')
        self.assertNotEqual(solution.interpret_western_sign(22, 12), 'sagittarius')

    def test_western_signs_capricorn(self):
        self.assertEqual(solution.interpret_western_sign(22, 12), 'capricorn')
        self.assertEqual(solution.interpret_western_sign(20, 1), 'capricorn')
        self.assertNotEqual(solution.interpret_western_sign(21, 12), 'capricorn')
        self.assertNotEqual(solution.interpret_western_sign(21, 1), 'capricorn')

    def test_chinese_signs_rat(self):
        self.assertEqual(solution.interpret_chinese_sign(1900), 'rat')
        self.assertEqual(solution.interpret_chinese_sign(1912), 'rat')

    def test_chinese_signs_ox(self):
        self.assertEqual(solution.interpret_chinese_sign(1901), 'ox')
        self.assertEqual(solution.interpret_chinese_sign(1913), 'ox')

    def test_chinese_signs_tiger(self):
        self.assertEqual(solution.interpret_chinese_sign(1902), 'tiger')
        self.assertEqual(solution.interpret_chinese_sign(1914), 'tiger')
        self.assertNotEqual(solution.interpret_chinese_sign(1901), 'tiger')

    def test_chinese_signs_rabbit(self):
        self.assertEqual(solution.interpret_chinese_sign(1903), 'rabbit')
        self.assertEqual(solution.interpret_chinese_sign(1915), 'rabbit')
        self.assertNotEqual(solution.interpret_chinese_sign(1902), 'rabbit')

    def test_chinese_signs_dragon(self):
        self.assertEqual(solution.interpret_chinese_sign(1904), 'dragon')
        self.assertEqual(solution.interpret_chinese_sign(1916), 'dragon')
        self.assertNotEqual(solution.interpret_chinese_sign(1903), 'dragon')

    def test_chinese_signs_snake(self):
        self.assertEqual(solution.interpret_chinese_sign(1905), 'snake')
        self.assertEqual(solution.interpret_chinese_sign(1917), 'snake')
        self.assertNotEqual(solution.interpret_chinese_sign(1904), 'snake')

    def test_chinese_signs_horse(self):
        self.assertEqual(solution.interpret_chinese_sign(1906), 'horse')
        self.assertEqual(solution.interpret_chinese_sign(1918), 'horse')
        self.assertNotEqual(solution.interpret_chinese_sign(1905), 'horse')

    def test_chinese_signs_sheep(self):
        self.assertEqual(solution.interpret_chinese_sign(1907), 'sheep')
        self.assertEqual(solution.interpret_chinese_sign(1919), 'sheep')
        self.assertNotEqual(solution.interpret_chinese_sign(1906), 'sheep')

    def test_chinese_signs_monkey(self):
        self.assertEqual(solution.interpret_chinese_sign(1908), 'monkey')
        self.assertEqual(solution.interpret_chinese_sign(1920), 'monkey')
        self.assertNotEqual(solution.interpret_chinese_sign(1907), 'monkey')

    def test_chinese_signs_rooster(self):
        self.assertEqual(solution.interpret_chinese_sign(1909), 'rooster')
        self.assertEqual(solution.interpret_chinese_sign(1921), 'rooster')
        self.assertNotEqual(solution.interpret_chinese_sign(1908), 'rooster')

    def test_chinese_signs_dog(self):
        self.assertEqual(solution.interpret_chinese_sign(1910), 'dog')
        self.assertEqual(solution.interpret_chinese_sign(1922), 'dog')
        self.assertNotEqual(solution.interpret_chinese_sign(1909), 'dog')

    def test_chinese_signs_pig(self):
        self.assertEqual(solution.interpret_chinese_sign(1911), 'pig')
        self.assertEqual(solution.interpret_chinese_sign(1923), 'pig')
        self.assertNotEqual(solution.interpret_chinese_sign(1910), 'pig')

    def test_intersect_taurus_snake(self):
        self.assertEqual(
            solution.interpret_both_signs(8, 5, 1989),
            ('taurus', 'snake')
        )
        self.assertEqual(
            solution.interpret_both_signs(20, 5, 2001),
            ('taurus', 'snake')
        )
        self.assertNotEqual(
            solution.interpret_both_signs(8, 5, 1988),
            ('taurus', 'snake')
        )

    def test_intersect_aries_dragon(self):
        self.assertEqual(
            solution.interpret_both_signs(4, 4, 1940),
            ('aries', 'dragon')
        )
        self.assertEqual(
            solution.interpret_both_signs(4, 4, 1928),
            ('aries', 'dragon')
        )
        self.assertNotEqual(
            solution.interpret_both_signs(4, 4, 1945),
            ('aries', 'dragon')
        )

    def test_intersect_aquarius_rat(self):
        self.assertEqual(
            solution.interpret_both_signs(1, 2, 1948),
            ('aquarius', 'rat')
        )
        self.assertEqual(
            solution.interpret_both_signs(1, 2, 1972),
            ('aquarius', 'rat')
        )
        self.assertNotEqual(
            solution.interpret_both_signs(1, 8, 1948),
            ('aquarius', 'rat')
        )

    def test_intersect_pisces_pig(self):
        self.assertEqual(
            solution.interpret_both_signs(1, 3, 1971),
            ('pisces', 'pig')
        )
        self.assertEqual(
            solution.interpret_both_signs(19, 2, 1971),
            ('pisces', 'pig')
        )
        self.assertNotEqual(
            solution.interpret_both_signs(21, 3, 1971),
            ('pisces', 'pig')
        )

    # not a good practice just showing that this is possbile too.
    # also noone posted tests with years before 1900 and after 2015 so.. yea
    def test_chinese_signs(self):
        self.assertEqual(solution.interpret_chinese_sign(2000), 'dragon')
        self.assertEqual(solution.interpret_chinese_sign(1994), 'dog')
        self.assertEqual(solution.interpret_chinese_sign(1992), 'monkey')
        self.assertEqual(solution.interpret_chinese_sign(1893), 'snake')
        self.assertEqual(solution.interpret_chinese_sign(1723), 'rabbit')
        self.assertEqual(solution.interpret_chinese_sign(982), 'horse')
        self.assertEqual(solution.interpret_chinese_sign(123), 'pig')
        self.assertEqual(solution.interpret_chinese_sign(124), 'rat')
        self.assertEqual(solution.interpret_chinese_sign(11285), 'ox')
        self.assertEqual(solution.interpret_chinese_sign(2015), 'sheep')
        self.assertEqual(solution.interpret_chinese_sign(2017), 'rooster')
        self.assertEqual(solution.interpret_chinese_sign(-547), 'ox')


if __name__ == '__main__':
    unittest.main()
