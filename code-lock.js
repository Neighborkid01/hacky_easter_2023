nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

function bruteForce() {
  for (let a = 0; a < nums.length; a++) {
    code = nums[a];
    let code_a = code;
    for (let b = 0; b < nums.length; b++) {
      code = code_a + nums[b];
      let code_b = code;
      for (let c = 0; c < nums.length; c++) {
        code = code_b + nums[c];
        let code_c = code;
        for (let d = 0; d < nums.length; d++) {
          code = code_c + nums[d];
          let code_d = code;
          for (let e = 0; e < nums.length; e++) {
            code = code_d + nums[e];
            let code_e = code;
            for (let f = 0; f < nums.length; f++) {
              code = code_e + nums[f];
              let code_f = code;
              for (let g = 0; g < nums.length; g++) {
                code = code_f + nums[g];
                let code_g = code;
                for (let h = 0; h < nums.length; h++) {
                  code = code_g + nums[h];
                  let code_h = code;
                  res = checkWASM(code);
                  if (res.startsWith("he2023")) {
                    console.log(code);
                    console.log(res);
                    return;
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}