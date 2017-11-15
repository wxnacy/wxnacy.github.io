" if exists("b:current_syntax")
    " finish
" endif

syntax keyword potionKeyword class self def
syntax keyword potionKeyword from import
syntax keyword potionKeyword __name__
syntax keyword potionFunction print join string
" syntax match potionComment "\v#.*$"
" syn keyword potionKeyword contained TODO FIXME NOTE
" syn match potionComment "\v#.*$" contains=potionKeyword
" syntax match potionOperator "\v\*"
" syntax match potionOperator "\v/"
" syntax match potionOperator "\v\+"
" syntax match potionOperator "\v-"
" syntax match potionOperator "\v\?"
" syntax match potionOperator "\v\*\="
" syntax match potionOperator "\v/\="
" syntax match potionOperator "\v\+\="
" syntax match potionOperator "\v-\="

highlight! link potionKeyword Keyword
highlight! link potionFunction Function
" highlight! link potionComment Comment
" highlight! link potionOperator Operator


" let b:current_syntax = "potion"
