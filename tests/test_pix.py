import sys
sys.path.append("../")


import pytest
import os
from payments.pix import Pix

def test_create_payment_pix():
  pix_instance = Pix()

  #create_payment
  payment_info = pix_instance.create_payment("../")
 
  assert "bank_payment_id" in payment_info
  assert "qr_code_path" in payment_info

  qr_code_path = payment_info['qr_code_path']
  assert os.path.isfile(f"../static/img/{qr_code_path}.png")
  os.remove(f"../static/img/{qr_code_path}.png")

