from rich import print
import fire
import tensorflow as tf

def convolution(input_size=(256,256,512), num_filters=256, filter_size=3, stride=1, padding='same'):

  if padding == 'same':
    pad = 2*((filter_size-1)/2)
    out_size = int((input_size[0] - filter_size + pad) / stride + 1)
  elif padding == 'valid':
    out_size = int((input_size[0] - filter_size) / stride + 1)
    
  out_tuple = (out_size, out_size, num_filters)
  print(f"[bold magenta]Input:{input_size}[/bold magenta] :right_arrow: [bold green]Output:{out_tuple}[/bold green]")
  return

if __name__ == '__main__':
  fire.Fire(convolution)