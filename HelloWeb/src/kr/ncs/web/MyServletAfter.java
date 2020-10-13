package kr.ncs.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class MyServletAfter
 */
@WebServlet("/after")
public class MyServletAfter extends HttpServlet {
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		PrintWriter out = response.getWriter();
		boolean flag = true;
		if(flag) {
			out.println("<html>");
			out.println("<head>");
			out.println("<body>");
			out.println("	<div>hello</div>");
			out.println("</body>");
			out.println("</head>");
			out.println("</html>");
		}else {
			out.println("<html>");
			out.println("<head>");
			out.println("<body>");
			out.println("	<div>ng</div>");
			out.println("</body>");
			out.println("</head>");
			out.println("</html>");
		}
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
	}

}
