def getPipeline(stage):
  stages = {
    # Adquirencia
    "62ec343cd0e468000c4302ce": [
      '62ec343cd0e468000c4302cf',
      '62ec343cd0e468000c4302d0',
      '62ec343cd0e468000c4302d2',
      '62ec343cd0e468000c4302d3',
      '62ec34da193d6e000c8c4325',
      '62ec34edd0878c001bcf7359',
    ],
    # Credit
    "6438012fcd94620011109594": [
      '6438012fcd94620011109595',
      '6438012fcd94620011109596',
      '6438012fcd94620011109597',
      '6438012fcd94620011109598',
      '6438012fcd94620011109599',
      '64380193c5d0520018e1849d',
      '643801e936710a0016bfa43f',
      '643801f3cae7760026f683b4',
      '64d674fc8a6ce10027f1b174',
      '64d67485bb070d0011b93be9',
      '64d674999826ef002437bcc8',
      '64d674a531ec42001a1614ec',
    ],
  }
  for index, values in stages.items():
      for value in values:
         if stage == value:
            return index
  return '62bf235eff780b0010a37c28' # Pos-venda