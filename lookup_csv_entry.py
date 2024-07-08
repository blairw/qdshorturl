import pandas as pd

# Adapted from https://stackoverflow.com/questions/9161439/parse-key-value-pairs-in-a-text-file
secrets = {}
with open("secrets_csvmode.txt") as myfile:
	for line in myfile:
		key, value = line.partition("=")[::2]
		secrets[key.strip()] = value.strip()
		
def get_mapped_url(given_shortid):
  df_mappingfile = pd.read_csv(secrets["mappingfile_csv"])
  df_lookup_shortid = df_mappingfile[df_mappingfile['shortid'] == given_shortid]
  df_lookup_shortid_mapped_url = df_lookup_shortid[['mapped_url']]
  prepared_output = df_lookup_shortid_mapped_url.iloc[0, 0]

  return prepared_output
