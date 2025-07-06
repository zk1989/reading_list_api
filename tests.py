# TESTS FOR FUTURE IMPLEMENTATION
#
# import requests as r
# import unittest
# from parameterized import parameterized
#
#
# class TestApp(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.base_url = 'https://jsonplaceholder.typicode.com'
#         cls.sample_data = {'robot': '2', 'terminator': '3'}
#
#     def test_root_connection(self):
#         rs = r.get(self.base_url)
#         self.assertEqual(rs.status_code, 200)
#
#     def test_invalid_endpoint(self):
#         rs = r.get(self.base_url + '/nonexistent')
#         self.assertEqual(rs.status_code, 404)
#
#     def test_get_comments(self):
#         rs = r.get(self.base_url + "/comments")
#         self.assertIn('application/json', rs.headers['content-type'])
#         self.assertIsInstance(rs.json(), list)
#         self.assertGreater(len(rs.json()), 0)
#
#     def test_get_single_comment(self):
#         rs = r.get(self.base_url + "/comments/1")
#         comment = rs.json()
#         self.assertEqual(comment['id'], 1)
#         self.assertIn('name', comment)
#
#     def test_post_comment(self):
#         rs = r.post(self.base_url + "/comments", self.sample_data)
#         comments = rs.json()
#         self.assertEqual(rs.status_code, 201)
#         self.assertEqual(comments['robot'], '2')
#
#     @parameterized.expand([
#         ("text/plain", "gluliglagligi", 201),
#         ("image/png", "mkfdskfjksdfjks", 201)
#     ])
#     def test_post_comment_with_illegal_content_type(self, content_type, payload, expected_status_code):
#         headers = {'Content-Type': f'{content_type}'}
#         rs = r.post(self.base_url + "/comments", payload, headers=headers)
#         self.assertEqual(rs.status_code, expected_status_code)
#
#     def test_getting_payload(self):
#         payload = {'id': '3'}
#         rs = r.get(self.base_url + "/comments", params=payload)
#         self.assertTrue(rs)
