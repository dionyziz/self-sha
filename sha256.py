def A():
  return "def B(B_str):\n  def q(w):\n    def escape(x):\n      return x.replace('\\\\', '\\\\\\\\').replace('\"', '\\\\\"').replace('\\n', '\\\\n')\n\n    return \"def A():\\n  return \\\"\" + escape(w) + \"\\\"\"\n  \n  A_str = q(B_str)\n\n  SELF = \"{}\\n\\n{}\\n\\nB(A())\\n\".format(A_str, B_str)\n\n  import copy\n  import struct\n  import binascii\n\n  F32 = 0xFFFFFFFF\n\n  _k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,\n        0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,\n        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,\n        0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,\n        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,\n        0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,\n        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,\n        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,\n        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,\n        0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,\n        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,\n        0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,\n        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,\n        0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,\n        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,\n        0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]\n\n  _h = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,\n        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]\n\n  def _pad(msglen):\n      mdi = msglen & 0x3F\n      length = struct.pack('!Q', msglen << 3)\n\n      if mdi < 56:\n          padlen = 55 - mdi\n      else:\n          padlen = 119 - mdi\n\n      return b'\\x80' + (b'\\x00' * padlen) + length\n\n  def _rotr(x, y):\n      return ((x >> y) | (x << (32 - y))) & F32\n\n  def _maj(x, y, z):\n      return (x & y) ^ (x & z) ^ (y & z)\n\n  def _ch(x, y, z):\n      return (x & y) ^ ((~x) & z)\n\n  class SHA256:\n      _output_size = 8\n      blocksize = 1\n      block_size = 64\n      digest_size = 32\n\n      def __init__(self, m=None):\n          self._counter = 0\n          self._cache = b''\n          self._k = copy.deepcopy(_k)\n          self._h = copy.deepcopy(_h)\n\n          self.update(m)\n\n      def _compress(self, c):\n          w = [0] * 64\n          w[0:16] = struct.unpack('!16L', c)\n\n          for i in range(16, 64):\n              s0 = _rotr(w[i-15], 7) ^ _rotr(w[i-15], 18) ^ (w[i-15] >> 3)\n              s1 = _rotr(w[i-2], 17) ^ _rotr(w[i-2], 19) ^ (w[i-2] >> 10)\n              w[i] = (w[i-16] + s0 + w[i-7] + s1) & F32\n\n          a, b, c, d, e, f, g, h = self._h\n\n          for i in range(64):\n              s0 = _rotr(a, 2) ^ _rotr(a, 13) ^ _rotr(a, 22)\n              t2 = s0 + _maj(a, b, c)\n              s1 = _rotr(e, 6) ^ _rotr(e, 11) ^ _rotr(e, 25)\n              t1 = h + s1 + _ch(e, f, g) + self._k[i] + w[i]\n\n              h = g\n              g = f\n              f = e\n              e = (d + t1) & F32\n              d = c\n              c = b\n              b = a\n              a = (t1 + t2) & F32\n\n          for i, (x, y) in enumerate(zip(self._h, [a, b, c, d, e, f, g, h])):\n              self._h[i] = (x + y) & F32\n\n      def update(self, m):\n          if not m:\n              return\n\n          self._cache += m\n          self._counter += len(m)\n\n          while len(self._cache) >= 64:\n              self._compress(self._cache[:64])\n              self._cache = self._cache[64:]\n\n      def digest(self):\n          r = copy.deepcopy(self)\n          r.update(_pad(self._counter))\n          data = [struct.pack('!L', i) for i in r._h[:self._output_size]]\n          return b''.join(data)\n\n      def hexdigest(self):\n          return binascii.hexlify(self.digest()).decode('ascii')\n\n  m = SHA256()\n  m.update(SELF.encode('utf8'))\n  print(m.hexdigest())"

def B(B_str):
  def q(w):
    def escape(x):
      return x.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

    return "def A():\n  return \"" + escape(w) + "\""
  
  A_str = q(B_str)

  SELF = "{}\n\n{}\n\nB(A())\n".format(A_str, B_str)

  import copy
  import struct
  import binascii

  F32 = 0xFFFFFFFF

  _k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
        0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
        0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
        0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
        0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
        0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
        0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
        0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

  _h = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

  def _pad(msglen):
      mdi = msglen & 0x3F
      length = struct.pack('!Q', msglen << 3)

      if mdi < 56:
          padlen = 55 - mdi
      else:
          padlen = 119 - mdi

      return b'\x80' + (b'\x00' * padlen) + length

  def _rotr(x, y):
      return ((x >> y) | (x << (32 - y))) & F32

  def _maj(x, y, z):
      return (x & y) ^ (x & z) ^ (y & z)

  def _ch(x, y, z):
      return (x & y) ^ ((~x) & z)

  class SHA256:
      _output_size = 8
      blocksize = 1
      block_size = 64
      digest_size = 32

      def __init__(self, m=None):
          self._counter = 0
          self._cache = b''
          self._k = copy.deepcopy(_k)
          self._h = copy.deepcopy(_h)

          self.update(m)

      def _compress(self, c):
          w = [0] * 64
          w[0:16] = struct.unpack('!16L', c)

          for i in range(16, 64):
              s0 = _rotr(w[i-15], 7) ^ _rotr(w[i-15], 18) ^ (w[i-15] >> 3)
              s1 = _rotr(w[i-2], 17) ^ _rotr(w[i-2], 19) ^ (w[i-2] >> 10)
              w[i] = (w[i-16] + s0 + w[i-7] + s1) & F32

          a, b, c, d, e, f, g, h = self._h

          for i in range(64):
              s0 = _rotr(a, 2) ^ _rotr(a, 13) ^ _rotr(a, 22)
              t2 = s0 + _maj(a, b, c)
              s1 = _rotr(e, 6) ^ _rotr(e, 11) ^ _rotr(e, 25)
              t1 = h + s1 + _ch(e, f, g) + self._k[i] + w[i]

              h = g
              g = f
              f = e
              e = (d + t1) & F32
              d = c
              c = b
              b = a
              a = (t1 + t2) & F32

          for i, (x, y) in enumerate(zip(self._h, [a, b, c, d, e, f, g, h])):
              self._h[i] = (x + y) & F32

      def update(self, m):
          if not m:
              return

          self._cache += m
          self._counter += len(m)

          while len(self._cache) >= 64:
              self._compress(self._cache[:64])
              self._cache = self._cache[64:]

      def digest(self):
          r = copy.deepcopy(self)
          r.update(_pad(self._counter))
          data = [struct.pack('!L', i) for i in r._h[:self._output_size]]
          return b''.join(data)

      def hexdigest(self):
          return binascii.hexlify(self.digest()).decode('ascii')

  m = SHA256()
  m.update(SELF.encode('utf8'))
  print(m.hexdigest())

B(A())
