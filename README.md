A simple command line processor to convert CSV import from REdmine
into PDFs. Export the stories in CSV format by visiting a page that
has a list of stories, click on the CSV link on the bottom right. Pick
_All columns_, and also check _Description_. Save the `exports.csv`
file somewhere. Then run `print-stories export.csv`. This command
outputs to `stories.pdf`.