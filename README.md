# HipChatGerritHooks
Gerrit hooks sending notifications to HipChat

### Requirements
- Python 3

### Available hooks
- `reviewer-added` - sends private message to the reviewer
- `comment-added` - sends (colorful) room message with CodeReview score, if Verified score is set or change is a draft then nothing happens

### Configuration
Following options can be set in `'$site_path'/etc/hipchat.config`:
- `[general][auth_token]` - HipChat API token - **required**
- `[reviewer-added][ignored_emails]` - regular expression describing emails of users which should not receive `reviewer-added` notifications
See [sample config file](etc/hipchat.config).

### Notes
- room naming scheme is hardcoded to `<project> alerts` where `<project>` is the project name in Gerrit
- operation results are printed to `stdout`, so they are saved to `'$site_path'/logs/error_log`
- since config file contains API token it should have safe permissions eg. `0600`
- required API token scopes: `send_message`, `send_notification`
- hooks should be placed in `'$site_path'/hooks` and executable

## License
Apache License<br>
See [LICENSE](LICENSE) file.
