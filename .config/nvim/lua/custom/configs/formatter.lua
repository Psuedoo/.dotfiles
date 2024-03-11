local util = require "formatter.util"



require("formatter").setup({
  logging = true,
  log_level = vim.log.levels.DEBUG,

  filetype = {

    python = {
      require("formatter.filetypes.python").black,
    },

    html = {
      require("formatter.filetypes.html").prettier,
    },


    ["*"] = {
      require("formatter.filetypes.any").remove_trailing_whitespaces
    }
  }
})
