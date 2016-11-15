# Auto latex generator for counters

##Usage:
1. Test if you have necessary packages:
  ```
  $ which pdflatex
  $ which convert
  ```
  If you don't have it, install it.

2. Create virtualenv and install python packages:
  ```
  virtualenv -p python3.5 counter-env3
  . counter-env3/bin/activate
  pip install -r requirements.txt
  ```

3. Run server:
  ```
  cd web
  python server.py &
  ```

4. Visit site: `0.0.0.0:5000` in your browser.
5. Enjoy :)
