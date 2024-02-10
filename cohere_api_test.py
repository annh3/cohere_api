from absl import app
from absl import flags
import cohere

FLAGS = flags.FLAGS
flags.DEFINE_string('key', None, 'api key')

def main(argv):
  del argv
  co = cohere.Client(FLAGS.key)
  response = co.generate(prompt='Please explain to me how LLMs work')
  print(response)

if __name__ == '__main__':
  app.run(main)
