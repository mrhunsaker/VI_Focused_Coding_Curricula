// Populate the sidebar
//
// This is a script, and not included directly in the page, to control the total size of the book.
// The TOC contains an entry for each page, so if each page includes a copy of the TOC,
// the total size of the page becomes O(n**2).
class MDBookSidebarScrollbox extends HTMLElement {
    constructor() {
        super();
    }
    connectedCallback() {
        this.innerHTML = '<ol class="chapter"><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="OVERALL_README.html">Curriculum Overview</a></span></li><li class="chapter-item expanded "><li class="part-title">Preliminary prerequisite: Terminal navigation</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="TERMINAL/TERMINAL_README.html"><strong aria-hidden="true">1.</strong> Terminal skills overview</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="TERMINAL/bash.html"><strong aria-hidden="true">1.1.</strong> Bash navigation and syntax</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="TERMINAL/powershell.html"><strong aria-hidden="true">1.2.</strong> PowerShell navigation and syntax</a></span></li></ol><li class="chapter-item expanded "><li class="part-title">Development environment</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="DEVELOPMENT/IDE_SETUP.html"><strong aria-hidden="true">2.</strong> Standalone IDE setup: VS Code, VSCodium, and Theia</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="DEVELOPMENT/ENVIRONMENT_ISOLATION.html"><strong aria-hidden="true">2.1.</strong> Project environments, dependency management, and containers</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="DEVELOPMENT/GUI_VISUALIZATION_ACCESSIBILITY.html"><strong aria-hidden="true">2.2.</strong> Screen-reader-accessible GUI libraries and implementation guidance</a></span></li></ol><li class="chapter-item expanded "><li class="part-title">Foundations (complete before any language)</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="FOUNDATIONS/FOUNDATIONS_README.html"><strong aria-hidden="true">3.</strong> Foundations overview</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="FOUNDATIONS/unit-p-computing-foundations.html"><strong aria-hidden="true">3.1.</strong> Unit P: Computing Foundations Primer</a></span></li></ol><li class="chapter-item expanded "><li class="part-title">C</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="C/c_README.html"><strong aria-hidden="true">4.</strong> C Curriculum</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="C/lessons.html"><strong aria-hidden="true">4.1.</strong> All units index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="C/unit00-accessible-environment-and-toolchain.html"><strong aria-hidden="true">4.2.</strong> Unit 0</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="C/unit01-foundations-of-computing.html"><strong aria-hidden="true">4.3.</strong> Unit 1</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="C/unit02-numeric-computation.html"><strong aria-hidden="true">4.4.</strong> Unit 2</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="C/unit03-control-flow.html"><strong aria-hidden="true">4.5.</strong> Unit 3</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="C/unit04-data-structures.html"><strong aria-hidden="true">4.6.</strong> Unit 4</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="C/unit05-input-and-iteration.html"><strong aria-hidden="true">4.7.</strong> Unit 5</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="C/unit06-functions.html"><strong aria-hidden="true">4.8.</strong> Unit 6</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="C/unit07-structs-and-object-models.html"><strong aria-hidden="true">4.9.</strong> Unit 7</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="C/unit08-files-errors-and-persistence.html"><strong aria-hidden="true">4.10.</strong> Unit 8</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="C/unit09-testing-and-data-analysis.html"><strong aria-hidden="true">4.11.</strong> Unit 9</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="C/unit10-applied-projects.html"><strong aria-hidden="true">4.12.</strong> Unit 10</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="C/unit11-capstone-personal-data-manager.html"><strong aria-hidden="true">4.13.</strong> Unit 11</a></span></li></ol><li class="chapter-item expanded "><li class="part-title">C++ (C Plus Plus)</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="CPP/cpp_README.html"><strong aria-hidden="true">5.</strong> CPP Curriculum</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CPP/lessons.html"><strong aria-hidden="true">5.1.</strong> All units index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CPP/unit00-accessible-environment-and-toolchain.html"><strong aria-hidden="true">5.2.</strong> Unit 0</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CPP/unit01-foundations-of-computing.html"><strong aria-hidden="true">5.3.</strong> Unit 1</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CPP/unit02-numeric-computations.html"><strong aria-hidden="true">5.4.</strong> Unit 2</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CPP/unit03-control-flow.html"><strong aria-hidden="true">5.5.</strong> Unit 3</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CPP/unit04-data-structures.html"><strong aria-hidden="true">5.6.</strong> Unit 4</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CPP/unit05-input-and-iteration.html"><strong aria-hidden="true">5.7.</strong> Unit 5</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CPP/unit06-functions.html"><strong aria-hidden="true">5.8.</strong> Unit 6</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CPP/unit07-object-oriented-programming.html"><strong aria-hidden="true">5.9.</strong> Unit 7</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CPP/unit08-files-and-exceptions.html"><strong aria-hidden="true">5.10.</strong> Unit 8</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CPP/unit09-testing-and-data-analysis.html"><strong aria-hidden="true">5.11.</strong> Unit 9</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CPP/unit10-project-based-learning.html"><strong aria-hidden="true">5.12.</strong> Unit 10</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CPP/unit11-capstone.html"><strong aria-hidden="true">5.13.</strong> Unit 11</a></span></li></ol><li class="chapter-item expanded "><li class="part-title">C-SHARP</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="CSHARP/csharp_README.html"><strong aria-hidden="true">6.</strong> CSHARP Curriculum</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CSHARP/lessons.html"><strong aria-hidden="true">6.1.</strong> All units index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CSHARP/unit00-accessible-environment-and-toolchain.html"><strong aria-hidden="true">6.2.</strong> Unit 0</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CSHARP/unit01-foundations-of-computing.html"><strong aria-hidden="true">6.3.</strong> Unit 1</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CSHARP/unit02-numeric-computations.html"><strong aria-hidden="true">6.4.</strong> Unit 2</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CSHARP/unit03-control-flow.html"><strong aria-hidden="true">6.5.</strong> Unit 3</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CSHARP/unit04-data-structures.html"><strong aria-hidden="true">6.6.</strong> Unit 4</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CSHARP/unit05-input-and-iteration.html"><strong aria-hidden="true">6.7.</strong> Unit 5</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CSHARP/unit06-functions.html"><strong aria-hidden="true">6.8.</strong> Unit 6</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CSHARP/unit07-object-oriented-programming.html"><strong aria-hidden="true">6.9.</strong> Unit 7</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CSHARP/unit08-files-and-exceptions.html"><strong aria-hidden="true">6.10.</strong> Unit 8</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CSHARP/unit09-testing-and-data-analysis.html"><strong aria-hidden="true">6.11.</strong> Unit 9</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CSHARP/unit10-project-based-learning.html"><strong aria-hidden="true">6.12.</strong> Unit 10</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CSHARP/unit11-capstone.html"><strong aria-hidden="true">6.13.</strong> Unit 11</a></span></li></ol><li class="chapter-item expanded "><li class="part-title">GO</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="GO/GO_README.html"><strong aria-hidden="true">7.</strong> GO Curriculum</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="GO/lessons.html"><strong aria-hidden="true">7.1.</strong> All units index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="GO/unit00-accessible-environment-and-toolchain.html"><strong aria-hidden="true">7.2.</strong> Unit 0</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="GO/unit01-foundations-of-computing.html"><strong aria-hidden="true">7.3.</strong> Unit 1</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="GO/unit02-numeric-computations.html"><strong aria-hidden="true">7.4.</strong> Unit 2</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="GO/unit03-control-flow.html"><strong aria-hidden="true">7.5.</strong> Unit 3</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="GO/unit04-data-structures.html"><strong aria-hidden="true">7.6.</strong> Unit 4</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="GO/unit05-input-and-iteration.html"><strong aria-hidden="true">7.7.</strong> Unit 5</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="GO/unit06-functions.html"><strong aria-hidden="true">7.8.</strong> Unit 6</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="GO/unit07-object-oriented-programming-with-go-types.html"><strong aria-hidden="true">7.9.</strong> Unit 7</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="GO/unit08-files-and-exceptions.html"><strong aria-hidden="true">7.10.</strong> Unit 8</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="GO/unit09-testing-and-data-analysis.html"><strong aria-hidden="true">7.11.</strong> Unit 9</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="GO/unit10-project-based-learning-text-based-applications.html"><strong aria-hidden="true">7.12.</strong> Unit 10</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="GO/unit11-capstone-accessible-personal-data-manager.html"><strong aria-hidden="true">7.13.</strong> Unit 11</a></span></li></ol><li class="chapter-item expanded "><li class="part-title">JAVA</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="JAVA/JAVA_README.html"><strong aria-hidden="true">8.</strong> JAVA Curriculum</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVA/lessons.html"><strong aria-hidden="true">8.1.</strong> All units index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVA/unit00-accessible-java-development-environment.html"><strong aria-hidden="true">8.2.</strong> Unit 0</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVA/unit01-foundations-of-computing-and-java.html"><strong aria-hidden="true">8.3.</strong> Unit 1</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVA/unit02-numeric-computations.html"><strong aria-hidden="true">8.4.</strong> Unit 2</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVA/unit03-control-flow-decisions-and-loops.html"><strong aria-hidden="true">8.5.</strong> Unit 3</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVA/unit04-data-structures-lists-and-dictionaries.html"><strong aria-hidden="true">8.6.</strong> Unit 4</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVA/unit05-user-input-and-while-loops.html"><strong aria-hidden="true">8.7.</strong> Unit 5</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVA/unit06-functions-and-methods.html"><strong aria-hidden="true">8.8.</strong> Unit 6</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVA/unit07-classes-and-object-oriented-programming.html"><strong aria-hidden="true">8.9.</strong> Unit 7</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVA/unit08-files-and-exceptions.html"><strong aria-hidden="true">8.10.</strong> Unit 8</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVA/unit09-testing-and-data-analysis.html"><strong aria-hidden="true">8.11.</strong> Unit 9</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVA/unit10-project-based-learning-text-applications.html"><strong aria-hidden="true">8.12.</strong> Unit 10</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVA/unit11-capstone-accessible-personal-data-manager.html"><strong aria-hidden="true">8.13.</strong> Unit 11</a></span></li></ol><li class="chapter-item expanded "><li class="part-title">JAVASCRIPT</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="JAVASCRIPT/JAVASCRIPT_README.html"><strong aria-hidden="true">9.</strong> JAVASCRIPT Curriculum</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVASCRIPT/lessons.html"><strong aria-hidden="true">9.1.</strong> All units index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVASCRIPT/unit00-setting-up-your-javascript-development-environment.html"><strong aria-hidden="true">9.2.</strong> Unit 0</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVASCRIPT/unit01-foundations-getting-started-with-javascript.html"><strong aria-hidden="true">9.3.</strong> Unit 1</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVASCRIPT/unit02-numeric-computations-and-input-output.html"><strong aria-hidden="true">9.4.</strong> Unit 2</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVASCRIPT/unit03-control-flow-decisions-lists-and-strings.html"><strong aria-hidden="true">9.5.</strong> Unit 3</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVASCRIPT/unit04-data-structures-arrays-fixed-sequences-and-objects.html"><strong aria-hidden="true">9.6.</strong> Unit 4</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVASCRIPT/unit05-user-input-and-while-loops.html"><strong aria-hidden="true">9.7.</strong> Unit 5</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVASCRIPT/unit06-functions.html"><strong aria-hidden="true">9.8.</strong> Unit 6</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVASCRIPT/unit07-classes-and-object-oriented-programming.html"><strong aria-hidden="true">9.9.</strong> Unit 7</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVASCRIPT/unit08-files-and-exceptions.html"><strong aria-hidden="true">9.10.</strong> Unit 8</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVASCRIPT/unit09-testing-and-data-analysis.html"><strong aria-hidden="true">9.11.</strong> Unit 9</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVASCRIPT/unit10-project-based-learning-text-based-applications.html"><strong aria-hidden="true">9.12.</strong> Unit 10</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVASCRIPT/unit11-capstone-project-accessible-personal-data-manager.html"><strong aria-hidden="true">9.13.</strong> Unit 11</a></span></li></ol><li class="chapter-item expanded "><li class="part-title">JULIA</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="JULIA/julia_README.html"><strong aria-hidden="true">10.</strong> JULIA Curriculum</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JULIA/lessons.html"><strong aria-hidden="true">10.1.</strong> All units index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JULIA/unit00-accessible-environment-and-toolchain.html"><strong aria-hidden="true">10.2.</strong> Unit 0</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JULIA/unit01-foundations-of-computing.html"><strong aria-hidden="true">10.3.</strong> Unit 1</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JULIA/unit02-numeric-computations.html"><strong aria-hidden="true">10.4.</strong> Unit 2</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JULIA/unit03-control-flow.html"><strong aria-hidden="true">10.5.</strong> Unit 3</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JULIA/unit04-data-structures.html"><strong aria-hidden="true">10.6.</strong> Unit 4</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JULIA/unit05-input-and-iteration.html"><strong aria-hidden="true">10.7.</strong> Unit 5</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JULIA/unit06-functions.html"><strong aria-hidden="true">10.8.</strong> Unit 6</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JULIA/unit07-object-oriented-programming.html"><strong aria-hidden="true">10.9.</strong> Unit 7</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JULIA/unit08-files-and-exceptions.html"><strong aria-hidden="true">10.10.</strong> Unit 8</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JULIA/unit09-testing-and-data-analysis.html"><strong aria-hidden="true">10.11.</strong> Unit 9</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JULIA/unit10-project-based-learning.html"><strong aria-hidden="true">10.12.</strong> Unit 10</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JULIA/unit11-capstone.html"><strong aria-hidden="true">10.13.</strong> Unit 11</a></span></li></ol><li class="chapter-item expanded "><li class="part-title">KOTLIN</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="KOTLIN/KOTLIN_README.html"><strong aria-hidden="true">11.</strong> KOTLIN Curriculum</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="KOTLIN/lessons.html"><strong aria-hidden="true">11.1.</strong> All units index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="KOTLIN/unit00-accessible-development-environment.html"><strong aria-hidden="true">11.2.</strong> Unit 0</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="KOTLIN/unit01-foundations-of-computing.html"><strong aria-hidden="true">11.3.</strong> Unit 1</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="KOTLIN/unit02-numeric-computations.html"><strong aria-hidden="true">11.4.</strong> Unit 2</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="KOTLIN/unit03-control-flow-decisions-and-loops.html"><strong aria-hidden="true">11.5.</strong> Unit 3</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="KOTLIN/unit04-data-structures-lists-and-dictionaries.html"><strong aria-hidden="true">11.6.</strong> Unit 4</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="KOTLIN/unit05-user-input-and-while-loops.html"><strong aria-hidden="true">11.7.</strong> Unit 5</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="KOTLIN/unit06-functions.html"><strong aria-hidden="true">11.8.</strong> Unit 6</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="KOTLIN/unit07-classes-and-object-oriented-programming.html"><strong aria-hidden="true">11.9.</strong> Unit 7</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="KOTLIN/unit08-files-and-exceptions.html"><strong aria-hidden="true">11.10.</strong> Unit 8</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="KOTLIN/unit09-testing-and-data-analysis.html"><strong aria-hidden="true">11.11.</strong> Unit 9</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="KOTLIN/unit10-project-based-learning-text-based-applications.html"><strong aria-hidden="true">11.12.</strong> Unit 10</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="KOTLIN/unit11-capstone-accessible-personal-data-manager.html"><strong aria-hidden="true">11.13.</strong> Unit 11</a></span></li></ol><li class="chapter-item expanded "><li class="part-title">LUA</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="LUA/LUA_README.html"><strong aria-hidden="true">12.</strong> LUA Curriculum</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="LUA/lessons.html"><strong aria-hidden="true">12.1.</strong> All units index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="LUA/unit00-accessible-environment-and-toolchain.html"><strong aria-hidden="true">12.2.</strong> Unit 0</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="LUA/unit01-foundations-of-computing.html"><strong aria-hidden="true">12.3.</strong> Unit 1</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="LUA/unit02-numeric-computations.html"><strong aria-hidden="true">12.4.</strong> Unit 2</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="LUA/unit03-control-flow-decisions-and-loops.html"><strong aria-hidden="true">12.5.</strong> Unit 3</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="LUA/unit04-data-structures-lists-and-dictionaries.html"><strong aria-hidden="true">12.6.</strong> Unit 4</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="LUA/unit05-user-input-and-while-loops.html"><strong aria-hidden="true">12.7.</strong> Unit 5</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="LUA/unit06-functions.html"><strong aria-hidden="true">12.8.</strong> Unit 6</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="LUA/unit07-classes-and-object-oriented-programming.html"><strong aria-hidden="true">12.9.</strong> Unit 7</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="LUA/unit08-files-and-exceptions.html"><strong aria-hidden="true">12.10.</strong> Unit 8</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="LUA/unit09-testing-and-data-analysis.html"><strong aria-hidden="true">12.11.</strong> Unit 9</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="LUA/unit10-project-based-learning-text-based-applications.html"><strong aria-hidden="true">12.12.</strong> Unit 10</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="LUA/unit11-capstone-accessible-personal-data-manager.html"><strong aria-hidden="true">12.13.</strong> Unit 11</a></span></li></ol><li class="chapter-item expanded "><li class="part-title">PYTHON</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="PYTHON/PYTHON_README.html"><strong aria-hidden="true">13.</strong> PYTHON Curriculum</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="PYTHON/lessons.html"><strong aria-hidden="true">13.1.</strong> All units index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="PYTHON/unit00-setting-up-your-accessible-python-development-environme.html"><strong aria-hidden="true">13.2.</strong> Unit 0</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="PYTHON/unit01-foundations-of-computing-and-getting-started-with-pytho.html"><strong aria-hidden="true">13.3.</strong> Unit 1</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="PYTHON/unit02-writing-simple-programs-and-numeric-computations.html"><strong aria-hidden="true">13.4.</strong> Unit 2</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="PYTHON/unit03-control-flow-decisions-and-loops.html"><strong aria-hidden="true">13.5.</strong> Unit 3</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="PYTHON/unit04-data-structures-lists-and-dictionaries.html"><strong aria-hidden="true">13.6.</strong> Unit 4</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="PYTHON/unit05-user-input-and-while-loops.html"><strong aria-hidden="true">13.7.</strong> Unit 5</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="PYTHON/unit06-functions.html"><strong aria-hidden="true">13.8.</strong> Unit 6</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="PYTHON/unit07-classes-and-object-oriented-programming.html"><strong aria-hidden="true">13.9.</strong> Unit 7</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="PYTHON/unit08-files-and-exceptions.html"><strong aria-hidden="true">13.10.</strong> Unit 8</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="PYTHON/unit09-testing-and-data-analysis.html"><strong aria-hidden="true">13.11.</strong> Unit 9</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="PYTHON/unit10-project-based-learning-building-text-based-applications.html"><strong aria-hidden="true">13.12.</strong> Unit 10</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="PYTHON/unit11-capstone-project-accessible-personal-data-manager.html"><strong aria-hidden="true">13.13.</strong> Unit 11</a></span></li></ol><li class="chapter-item expanded "><li class="part-title">RUST</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="RUST/rust_README.html"><strong aria-hidden="true">14.</strong> RUST Curriculum</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="RUST/lessons.html"><strong aria-hidden="true">14.1.</strong> All units index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="RUST/unit00-accessible-environment-and-toolchain.html"><strong aria-hidden="true">14.2.</strong> Unit 0</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="RUST/unit01-foundations-of-computing.html"><strong aria-hidden="true">14.3.</strong> Unit 1</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="RUST/unit02-numeric-computations.html"><strong aria-hidden="true">14.4.</strong> Unit 2</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="RUST/unit03-control-flow.html"><strong aria-hidden="true">14.5.</strong> Unit 3</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="RUST/unit04-data-structures.html"><strong aria-hidden="true">14.6.</strong> Unit 4</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="RUST/unit05-input-and-iteration.html"><strong aria-hidden="true">14.7.</strong> Unit 5</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="RUST/unit06-functions.html"><strong aria-hidden="true">14.8.</strong> Unit 6</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="RUST/unit07-data-modeling-and-traits.html"><strong aria-hidden="true">14.9.</strong> Unit 7</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="RUST/unit08-files-and-error-handling.html"><strong aria-hidden="true">14.10.</strong> Unit 8</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="RUST/unit09-testing-and-data-analysis.html"><strong aria-hidden="true">14.11.</strong> Unit 9</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="RUST/unit10-project-based-learning.html"><strong aria-hidden="true">14.12.</strong> Unit 10</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="RUST/unit11-capstone.html"><strong aria-hidden="true">14.13.</strong> Unit 11</a></span></li></ol><li class="chapter-item expanded "><li class="part-title">SWIFT</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="SWIFT/swift_README.html"><strong aria-hidden="true">15.</strong> SWIFT Curriculum</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="SWIFT/lessons.html"><strong aria-hidden="true">15.1.</strong> All units index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="SWIFT/unit00-accessible-environment-and-toolchain.html"><strong aria-hidden="true">15.2.</strong> Unit 0</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="SWIFT/unit01-foundations-of-computing.html"><strong aria-hidden="true">15.3.</strong> Unit 1</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="SWIFT/unit02-numeric-computations.html"><strong aria-hidden="true">15.4.</strong> Unit 2</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="SWIFT/unit03-control-flow.html"><strong aria-hidden="true">15.5.</strong> Unit 3</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="SWIFT/unit04-data-structures.html"><strong aria-hidden="true">15.6.</strong> Unit 4</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="SWIFT/unit05-input-and-iteration.html"><strong aria-hidden="true">15.7.</strong> Unit 5</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="SWIFT/unit06-functions.html"><strong aria-hidden="true">15.8.</strong> Unit 6</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="SWIFT/unit07-object-oriented-programming.html"><strong aria-hidden="true">15.9.</strong> Unit 7</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="SWIFT/unit08-files-and-exceptions.html"><strong aria-hidden="true">15.10.</strong> Unit 8</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="SWIFT/unit09-testing-and-data-analysis.html"><strong aria-hidden="true">15.11.</strong> Unit 9</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="SWIFT/unit10-project-based-learning.html"><strong aria-hidden="true">15.12.</strong> Unit 10</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="SWIFT/unit11-capstone.html"><strong aria-hidden="true">15.13.</strong> Unit 11</a></span></li></ol><li class="chapter-item expanded "><li class="part-title">TYPESCRIPT</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="TYPESCRIPT/TYPESCRIPT_README.html"><strong aria-hidden="true">16.</strong> TYPESCRIPT Curriculum</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="TYPESCRIPT/lessons.html"><strong aria-hidden="true">16.1.</strong> All units index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="TYPESCRIPT/unit00-accessible-development-environment.html"><strong aria-hidden="true">16.2.</strong> Unit 0</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="TYPESCRIPT/unit01-foundations-of-computing.html"><strong aria-hidden="true">16.3.</strong> Unit 1</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="TYPESCRIPT/unit02-numeric-computations.html"><strong aria-hidden="true">16.4.</strong> Unit 2</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="TYPESCRIPT/unit03-control-flow-decisions-and-loops.html"><strong aria-hidden="true">16.5.</strong> Unit 3</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="TYPESCRIPT/unit04-data-structures-arrays-tuples-and-objects.html"><strong aria-hidden="true">16.6.</strong> Unit 4</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="TYPESCRIPT/unit05-user-input-and-while-loops.html"><strong aria-hidden="true">16.7.</strong> Unit 5</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="TYPESCRIPT/unit06-functions.html"><strong aria-hidden="true">16.8.</strong> Unit 6</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="TYPESCRIPT/unit07-classes-and-object-oriented-programming.html"><strong aria-hidden="true">16.9.</strong> Unit 7</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="TYPESCRIPT/unit08-files-and-exceptions.html"><strong aria-hidden="true">16.10.</strong> Unit 8</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="TYPESCRIPT/unit09-testing-and-data-analysis.html"><strong aria-hidden="true">16.11.</strong> Unit 9</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="TYPESCRIPT/unit10-project-based-learning-text-based-applications.html"><strong aria-hidden="true">16.12.</strong> Unit 10</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="TYPESCRIPT/unit11-capstone-accessible-personal-data-manager.html"><strong aria-hidden="true">16.13.</strong> Unit 11</a></span></li></ol><li class="chapter-item expanded "><li class="part-title">Standalone Topics/Languages</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="MODULES/index.html"><strong aria-hidden="true">17.</strong> Standalone Topics/Languages Resources</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="MODULES/GIT.html"><strong aria-hidden="true">17.1.</strong> Git and Version Control</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="MODULES/HTML_CSS.html"><strong aria-hidden="true">17.2.</strong> HTML and CSS</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="MODULES/WEB_ACCESSIBILITY.html"><strong aria-hidden="true">17.3.</strong> Web Accessibility</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="MODULES/MARKDOWN.html"><strong aria-hidden="true">17.4.</strong> Markdown Syntax</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="MODULES/R.html"><strong aria-hidden="true">17.5.</strong> R: Statistical Computing</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="MODULES/REGEX.html"><strong aria-hidden="true">17.6.</strong> Regular Expressions</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="MODULES/SQL.html"><strong aria-hidden="true">17.7.</strong> SQL: Relational Databases</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="MODULES/STRUCTURED_DATA.html"><strong aria-hidden="true">17.8.</strong> Structured Data (JSON, YAML, TOML)</a></span></li></ol><li class="chapter-item expanded "><li class="part-title">Backmatter</li></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="backmatter/Teachers-Guides.html"><strong aria-hidden="true">18.</strong> Teacher&#39;s Guides</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="C/teachers-guide.html"><strong aria-hidden="true">18.1.</strong> C Teacher&#39;s Guide</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CSHARP/teachers-guide.html"><strong aria-hidden="true">18.2.</strong> C# Teacher&#39;s Guide</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CPP/teachers-guide.html"><strong aria-hidden="true">18.3.</strong> C++ Teacher&#39;s Guide</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="GO/teachers-guide.html"><strong aria-hidden="true">18.4.</strong> Go Teacher&#39;s Guide</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVA/teachers-guide.html"><strong aria-hidden="true">18.5.</strong> Java Teacher&#39;s Guide</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVASCRIPT/teachers-guide.html"><strong aria-hidden="true">18.6.</strong> JavaScript Teacher&#39;s Guide</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JULIA/teachers-guide.html"><strong aria-hidden="true">18.7.</strong> Julia Teacher&#39;s Guide</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="KOTLIN/teachers-guide.html"><strong aria-hidden="true">18.8.</strong> Kotlin Teacher&#39;s Guide</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="LUA/teachers-guide.html"><strong aria-hidden="true">18.9.</strong> Lua Teacher&#39;s Guide</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="PYTHON/teachers-guide.html"><strong aria-hidden="true">18.10.</strong> Python Teacher&#39;s Guide</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="RUST/teachers-guide.html"><strong aria-hidden="true">18.11.</strong> Rust Teacher&#39;s Guide</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="SWIFT/teachers-guide.html"><strong aria-hidden="true">18.12.</strong> Swift Teacher&#39;s Guide</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="TYPESCRIPT/teachers-guide.html"><strong aria-hidden="true">18.13.</strong> TypeScript Teacher&#39;s Guide</a></span></li></ol><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="backmatter/GLOSSARY.html"><strong aria-hidden="true">19.</strong> Programming Code Glossary</a></span></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="backmatter/index.html"><strong aria-hidden="true">20.</strong> Index</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="C/INDEX.html"><strong aria-hidden="true">20.1.</strong> C Index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CSHARP/INDEX.html"><strong aria-hidden="true">20.2.</strong> C# Index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="CPP/INDEX.html"><strong aria-hidden="true">20.3.</strong> C++ Index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="GO/INDEX.html"><strong aria-hidden="true">20.4.</strong> Go Topic Index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVA/INDEX.html"><strong aria-hidden="true">20.5.</strong> Java Index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JAVASCRIPT/INDEX.html"><strong aria-hidden="true">20.6.</strong> JavaScript Index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="JULIA/INDEX.html"><strong aria-hidden="true">20.7.</strong> Julia Topic Index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="KOTLIN/INDEX.html"><strong aria-hidden="true">20.8.</strong> Kotlin Topic Index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="LUA/INDEX.html"><strong aria-hidden="true">20.9.</strong> Lua Topic Index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="PYTHON/INDEX.html"><strong aria-hidden="true">20.10.</strong> Python Index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="RUST/INDEX.html"><strong aria-hidden="true">20.11.</strong> Rust Topic Index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="MODULES/INDEX.html"><strong aria-hidden="true">20.12.</strong> Standalone Topics Index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="SWIFT/INDEX.html"><strong aria-hidden="true">20.13.</strong> Swift Topic Index</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="TYPESCRIPT/INDEX.html"><strong aria-hidden="true">20.14.</strong> TypeScript Index</a></span></li></ol><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="backmatter/Contributors.html"><strong aria-hidden="true">21.</strong> About The Author</a></span></li></ol>';
        // Set the current, active page, and reveal it if it's hidden
        let current_page = document.location.href.toString().split('#')[0].split('?')[0];
        if (current_page.endsWith('/')) {
            current_page += 'index.html';
        }
        const links = Array.prototype.slice.call(this.querySelectorAll('a'));
        const l = links.length;
        for (let i = 0; i < l; ++i) {
            const link = links[i];
            const href = link.getAttribute('href');
            if (href && !href.startsWith('#') && !/^(?:[a-z+]+:)?\/\//.test(href)) {
                link.href = path_to_root + href;
            }
            // The 'index' page is supposed to alias the first chapter in the book.
            // Check both with and without the '.html' suffix to be robust against pretty URLs
            if (link.href.replace(/\.html$/, '') === current_page.replace(/\.html$/, '')
                || i === 0
                && path_to_root === ''
                && current_page.endsWith('/index.html')) {
                link.classList.add('active');
                let parent = link.parentElement;
                while (parent) {
                    if (parent.tagName === 'LI' && parent.classList.contains('chapter-item')) {
                        parent.classList.add('expanded');
                    }
                    parent = parent.parentElement;
                }
            }
        }
        // Track and set sidebar scroll position
        this.addEventListener('click', e => {
            if (e.target.tagName === 'A') {
                const clientRect = e.target.getBoundingClientRect();
                const sidebarRect = this.getBoundingClientRect();
                sessionStorage.setItem('sidebar-scroll-offset', clientRect.top - sidebarRect.top);
            }
        }, { passive: true });
        const sidebarScrollOffset = sessionStorage.getItem('sidebar-scroll-offset');
        sessionStorage.removeItem('sidebar-scroll-offset');
        if (sidebarScrollOffset !== null) {
            // preserve sidebar scroll position when navigating via links within sidebar
            const activeSection = this.querySelector('.active');
            if (activeSection) {
                const clientRect = activeSection.getBoundingClientRect();
                const sidebarRect = this.getBoundingClientRect();
                const currentOffset = clientRect.top - sidebarRect.top;
                this.scrollTop += currentOffset - parseFloat(sidebarScrollOffset);
            }
        } else {
            // scroll sidebar to current active section when navigating via
            // 'next/previous chapter' buttons
            const activeSection = document.querySelector('#mdbook-sidebar .active');
            if (activeSection) {
                activeSection.scrollIntoView({ block: 'center' });
            }
        }
        // Toggle buttons
        const sidebarAnchorToggles = document.querySelectorAll('.chapter-fold-toggle');
        function toggleSection(ev) {
            ev.currentTarget.parentElement.parentElement.classList.toggle('expanded');
        }
        Array.from(sidebarAnchorToggles).forEach(el => {
            el.addEventListener('click', toggleSection);
        });
    }
}
window.customElements.define('mdbook-sidebar-scrollbox', MDBookSidebarScrollbox);


// ---------------------------------------------------------------------------
// Support for dynamically adding headers to the sidebar.

(function() {
    // This is used to detect which direction the page has scrolled since the
    // last scroll event.
    let lastKnownScrollPosition = 0;
    // This is the threshold in px from the top of the screen where it will
    // consider a header the "current" header when scrolling down.
    const defaultDownThreshold = 150;
    // Same as defaultDownThreshold, except when scrolling up.
    const defaultUpThreshold = 300;
    // The threshold is a virtual horizontal line on the screen where it
    // considers the "current" header to be above the line. The threshold is
    // modified dynamically to handle headers that are near the bottom of the
    // screen, and to slightly offset the behavior when scrolling up vs down.
    let threshold = defaultDownThreshold;
    // This is used to disable updates while scrolling. This is needed when
    // clicking the header in the sidebar, which triggers a scroll event. It
    // is somewhat finicky to detect when the scroll has finished, so this
    // uses a relatively dumb system of disabling scroll updates for a short
    // time after the click.
    let disableScroll = false;
    // Array of header elements on the page.
    let headers;
    // Array of li elements that are initially collapsed headers in the sidebar.
    // I'm not sure why eslint seems to have a false positive here.
    // eslint-disable-next-line prefer-const
    let headerToggles = [];
    // This is a debugging tool for the threshold which you can enable in the console.
    let thresholdDebug = false;

    // Updates the threshold based on the scroll position.
    function updateThreshold() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight;

        // The number of pixels below the viewport, at most documentHeight.
        // This is used to push the threshold down to the bottom of the page
        // as the user scrolls towards the bottom.
        const pixelsBelow = Math.max(0, documentHeight - (scrollTop + windowHeight));
        // The number of pixels above the viewport, at least defaultDownThreshold.
        // Similar to pixelsBelow, this is used to push the threshold back towards
        // the top when reaching the top of the page.
        const pixelsAbove = Math.max(0, defaultDownThreshold - scrollTop);
        // How much the threshold should be offset once it gets close to the
        // bottom of the page.
        const bottomAdd = Math.max(0, windowHeight - pixelsBelow - defaultDownThreshold);
        let adjustedBottomAdd = bottomAdd;

        // Adjusts bottomAdd for a small document. The calculation above
        // assumes the document is at least twice the windowheight in size. If
        // it is less than that, then bottomAdd needs to be shrunk
        // proportional to the difference in size.
        if (documentHeight < windowHeight * 2) {
            const maxPixelsBelow = documentHeight - windowHeight;
            const t = 1 - pixelsBelow / Math.max(1, maxPixelsBelow);
            const clamp = Math.max(0, Math.min(1, t));
            adjustedBottomAdd *= clamp;
        }

        let scrollingDown = true;
        if (scrollTop < lastKnownScrollPosition) {
            scrollingDown = false;
        }

        if (scrollingDown) {
            // When scrolling down, move the threshold up towards the default
            // downwards threshold position. If near the bottom of the page,
            // adjustedBottomAdd will offset the threshold towards the bottom
            // of the page.
            const amountScrolledDown = scrollTop - lastKnownScrollPosition;
            const adjustedDefault = defaultDownThreshold + adjustedBottomAdd;
            threshold = Math.max(adjustedDefault, threshold - amountScrolledDown);
        } else {
            // When scrolling up, move the threshold down towards the default
            // upwards threshold position. If near the bottom of the page,
            // quickly transition the threshold back up where it normally
            // belongs.
            const amountScrolledUp = lastKnownScrollPosition - scrollTop;
            const adjustedDefault = defaultUpThreshold - pixelsAbove
                + Math.max(0, adjustedBottomAdd - defaultDownThreshold);
            threshold = Math.min(adjustedDefault, threshold + amountScrolledUp);
        }

        if (documentHeight <= windowHeight) {
            threshold = 0;
        }

        if (thresholdDebug) {
            const id = 'mdbook-threshold-debug-data';
            let data = document.getElementById(id);
            if (data === null) {
                data = document.createElement('div');
                data.id = id;
                data.style.cssText = `
                    position: fixed;
                    top: 50px;
                    right: 10px;
                    background-color: 0xeeeeee;
                    z-index: 9999;
                    pointer-events: none;
                `;
                document.body.appendChild(data);
            }
            data.innerHTML = `
                <table>
                  <tr><td>documentHeight</td><td>${documentHeight.toFixed(1)}</td></tr>
                  <tr><td>windowHeight</td><td>${windowHeight.toFixed(1)}</td></tr>
                  <tr><td>scrollTop</td><td>${scrollTop.toFixed(1)}</td></tr>
                  <tr><td>pixelsAbove</td><td>${pixelsAbove.toFixed(1)}</td></tr>
                  <tr><td>pixelsBelow</td><td>${pixelsBelow.toFixed(1)}</td></tr>
                  <tr><td>bottomAdd</td><td>${bottomAdd.toFixed(1)}</td></tr>
                  <tr><td>adjustedBottomAdd</td><td>${adjustedBottomAdd.toFixed(1)}</td></tr>
                  <tr><td>scrollingDown</td><td>${scrollingDown}</td></tr>
                  <tr><td>threshold</td><td>${threshold.toFixed(1)}</td></tr>
                </table>
            `;
            drawDebugLine();
        }

        lastKnownScrollPosition = scrollTop;
    }

    function drawDebugLine() {
        if (!document.body) {
            return;
        }
        const id = 'mdbook-threshold-debug-line';
        const existingLine = document.getElementById(id);
        if (existingLine) {
            existingLine.remove();
        }
        const line = document.createElement('div');
        line.id = id;
        line.style.cssText = `
            position: fixed;
            top: ${threshold}px;
            left: 0;
            width: 100vw;
            height: 2px;
            background-color: red;
            z-index: 9999;
            pointer-events: none;
        `;
        document.body.appendChild(line);
    }

    function mdbookEnableThresholdDebug() {
        thresholdDebug = true;
        updateThreshold();
        drawDebugLine();
    }

    window.mdbookEnableThresholdDebug = mdbookEnableThresholdDebug;

    // Updates which headers in the sidebar should be expanded. If the current
    // header is inside a collapsed group, then it, and all its parents should
    // be expanded.
    function updateHeaderExpanded(currentA) {
        // Add expanded to all header-item li ancestors.
        let current = currentA.parentElement;
        while (current) {
            if (current.tagName === 'LI' && current.classList.contains('header-item')) {
                current.classList.add('expanded');
            }
            current = current.parentElement;
        }
    }

    // Updates which header is marked as the "current" header in the sidebar.
    // This is done with a virtual Y threshold, where headers at or below
    // that line will be considered the current one.
    function updateCurrentHeader() {
        if (!headers || !headers.length) {
            return;
        }

        // Reset the classes, which will be rebuilt below.
        const els = document.getElementsByClassName('current-header');
        for (const el of els) {
            el.classList.remove('current-header');
        }
        for (const toggle of headerToggles) {
            toggle.classList.remove('expanded');
        }

        // Find the last header that is above the threshold.
        let lastHeader = null;
        for (const header of headers) {
            const rect = header.getBoundingClientRect();
            if (rect.top <= threshold) {
                lastHeader = header;
            } else {
                break;
            }
        }
        if (lastHeader === null) {
            lastHeader = headers[0];
            const rect = lastHeader.getBoundingClientRect();
            const windowHeight = window.innerHeight;
            if (rect.top >= windowHeight) {
                return;
            }
        }

        // Get the anchor in the summary.
        const href = '#' + lastHeader.id;
        const a = [...document.querySelectorAll('.header-in-summary')]
            .find(element => element.getAttribute('href') === href);
        if (!a) {
            return;
        }

        a.classList.add('current-header');

        updateHeaderExpanded(a);
    }

    // Updates which header is "current" based on the threshold line.
    function reloadCurrentHeader() {
        if (disableScroll) {
            return;
        }
        updateThreshold();
        updateCurrentHeader();
    }


    // When clicking on a header in the sidebar, this adjusts the threshold so
    // that it is located next to the header. This is so that header becomes
    // "current".
    function headerThresholdClick(event) {
        // See disableScroll description why this is done.
        disableScroll = true;
        setTimeout(() => {
            disableScroll = false;
        }, 100);
        // requestAnimationFrame is used to delay the update of the "current"
        // header until after the scroll is done, and the header is in the new
        // position.
        requestAnimationFrame(() => {
            requestAnimationFrame(() => {
                // Closest is needed because if it has child elements like <code>.
                const a = event.target.closest('a');
                const href = a.getAttribute('href');
                const targetId = href.substring(1);
                const targetElement = document.getElementById(targetId);
                if (targetElement) {
                    threshold = targetElement.getBoundingClientRect().bottom;
                    updateCurrentHeader();
                }
            });
        });
    }

    // Takes the nodes from the given head and copies them over to the
    // destination, along with some filtering.
    function filterHeader(source, dest) {
        const clone = source.cloneNode(true);
        clone.querySelectorAll('mark').forEach(mark => {
            mark.replaceWith(...mark.childNodes);
        });
        dest.append(...clone.childNodes);
    }

    // Scans page for headers and adds them to the sidebar.
    document.addEventListener('DOMContentLoaded', function() {
        const activeSection = document.querySelector('#mdbook-sidebar .active');
        if (activeSection === null) {
            return;
        }

        const main = document.getElementsByTagName('main')[0];
        headers = Array.from(main.querySelectorAll('h2, h3, h4, h5, h6'))
            .filter(h => h.id !== '' && h.children.length && h.children[0].tagName === 'A');

        if (headers.length === 0) {
            return;
        }

        // Build a tree of headers in the sidebar.

        const stack = [];

        const firstLevel = parseInt(headers[0].tagName.charAt(1));
        for (let i = 1; i < firstLevel; i++) {
            const ol = document.createElement('ol');
            ol.classList.add('section');
            if (stack.length > 0) {
                stack[stack.length - 1].ol.appendChild(ol);
            }
            stack.push({level: i + 1, ol: ol});
        }

        // The level where it will start folding deeply nested headers.
        const foldLevel = 3;

        for (let i = 0; i < headers.length; i++) {
            const header = headers[i];
            const level = parseInt(header.tagName.charAt(1));

            const currentLevel = stack[stack.length - 1].level;
            if (level > currentLevel) {
                // Begin nesting to this level.
                for (let nextLevel = currentLevel + 1; nextLevel <= level; nextLevel++) {
                    const ol = document.createElement('ol');
                    ol.classList.add('section');
                    const last = stack[stack.length - 1];
                    const lastChild = last.ol.lastChild;
                    // Handle the case where jumping more than one nesting
                    // level, which doesn't have a list item to place this new
                    // list inside of.
                    if (lastChild) {
                        lastChild.appendChild(ol);
                    } else {
                        last.ol.appendChild(ol);
                    }
                    stack.push({level: nextLevel, ol: ol});
                }
            } else if (level < currentLevel) {
                while (stack.length > 1 && stack[stack.length - 1].level > level) {
                    stack.pop();
                }
            }

            const li = document.createElement('li');
            li.classList.add('header-item');
            li.classList.add('expanded');
            if (level < foldLevel) {
                li.classList.add('expanded');
            }
            const span = document.createElement('span');
            span.classList.add('chapter-link-wrapper');
            const a = document.createElement('a');
            span.appendChild(a);
            a.href = '#' + header.id;
            a.classList.add('header-in-summary');
            filterHeader(header.children[0], a);
            a.addEventListener('click', headerThresholdClick);
            const nextHeader = headers[i + 1];
            if (nextHeader !== undefined) {
                const nextLevel = parseInt(nextHeader.tagName.charAt(1));
                if (nextLevel > level && level >= foldLevel) {
                    const toggle = document.createElement('a');
                    toggle.classList.add('chapter-fold-toggle');
                    toggle.classList.add('header-toggle');
                    toggle.addEventListener('click', () => {
                        li.classList.toggle('expanded');
                    });
                    const toggleDiv = document.createElement('div');
                    toggleDiv.textContent = '❱';
                    toggle.appendChild(toggleDiv);
                    span.appendChild(toggle);
                    headerToggles.push(li);
                }
            }
            li.appendChild(span);

            const currentParent = stack[stack.length - 1];
            currentParent.ol.appendChild(li);
        }

        const onThisPage = document.createElement('div');
        onThisPage.classList.add('on-this-page');
        onThisPage.append(stack[0].ol);
        const activeItemSpan = activeSection.parentElement;
        activeItemSpan.after(onThisPage);
    });

    document.addEventListener('DOMContentLoaded', reloadCurrentHeader);
    document.addEventListener('scroll', reloadCurrentHeader, { passive: true });
})();

