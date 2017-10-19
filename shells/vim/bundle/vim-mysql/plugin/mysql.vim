function! HelloWorld()
    echo "hello world"
endfunction

python << EOF
def hello():
    print('hello python')
EOF

function! Test()
python << EOF
import vim
cur_buf = vim.current.buffer
print "Lines: {0}".format(len(cur_buf))
print "Contents: {0}".format(cur_buf[-1])

print( vim.current.line )
print( vim.current.buffer )
print( vim.current.window )
print( vim.current.tabpage )
print( vim.current.range )

EOF
endfunction

command! -nargs=0 HelloWorld call HelloWorld()
command! -nargs=0 Hpy exec('py hello()')
command! -nargs=0 Test call Test()
