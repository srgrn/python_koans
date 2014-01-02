module.exports = function(grunt) {
	"use strict";
	grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    watch: {
		files: ['./koans/*.py'],
		tasks: ['pythonrun']
	}
    });
    
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('pythonrun',"runs the python comand",function(){

        var exec = require('child_process').exec;
        var cb = this.async();
        exec('python.exe ./contemplate_koans.py', {cwd: '.'}, function(err, stdout, stderr) {
            grunt.log.write(stdout);
            cb();
        });     
        
    });

};