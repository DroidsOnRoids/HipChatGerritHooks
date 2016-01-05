import unittest
import sys
import common


class TestStringMethods(unittest.TestCase):
    def test_parse_args_default_values(self):
        del sys.argv[1:]
        args, unknown = common.parse_args()
        self.assertIsNotNone(args.codeReviewScore)

    def test_parse_all_args(self):
        project_name = 'test'
        change_url = 'https://test'
        author = 'author'
        change_owner = 'owner@test.test'
        change_id = '123456'
        is_draft = 'true'
        verified = '1'
        code_review = '2'
        reviewer = 'test@test.test'

        del sys.argv[1:]
        existing_argv = sys.argv[1:]
        sys.argv += '--project', project_name, \
                    '--author', author, \
                    '--is-draft', is_draft, \
                    '--Verified', verified, \
                    '--Code-Review', code_review, \
                    '--change-url', change_url, \
                    '--change-owner', change_owner, \
                    '--change', change_id, \
                    '--reviewer', reviewer
        args, unknown = common.parse_args()

        self.assertEqual(args.project, project_name)
        self.assertEqual(args.author, author)
        self.assertEqual(args.verifiedScore, verified)
        self.assertEqual(args.codeReviewScore, code_review)
        self.assertEqual(args.changeUrl, change_url)
        self.assertEqual(args.changeOwner, change_owner)
        self.assertEqual(args.changeId, change_id)
        self.assertEqual(args.reviewer, reviewer)
        self.assertEqual(unknown, existing_argv)


if __name__ == '__main__':
    unittest.main()
