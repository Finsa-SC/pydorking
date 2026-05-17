query dorking disimpan di dalam file json dengan pengelompokan berdasarkan kategori nya

{
  "sensitive_data": [
    "filetype:sql \"password\" dump",
    "intitle:\"index of\" \"contacts.xlsx\"",
    "ext:log \"username\" \"password\""
  ],
  "user_credentials": [
    "inurl:login.php \"admin\"",
    "filetype:env \"DB_PASSWORD\"",
    "intitle:\"Dashboard\" \"Sign In\""
  ],
  "config_files": [
    "filetype:conf \"allow_anonymous=true\"",
    "ext:xml \"dbpassword\""
  ]
}