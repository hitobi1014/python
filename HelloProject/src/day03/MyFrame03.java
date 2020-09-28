package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyFrame03 extends JFrame {

	private JPanel contentPane;
	private JTextField firstNum;
	private JTextField secondNum;
	private JTextField result;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame03 frame = new MyFrame03();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MyFrame03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		firstNum = new JTextField();
		firstNum.setBounds(21, 56, 64, 21);
		contentPane.add(firstNum);
		firstNum.setColumns(10);
		
		secondNum = new JTextField();
		secondNum.setBounds(142, 56, 66, 21);
		contentPane.add(secondNum);
		secondNum.setColumns(10);
		
		JLabel lbl = new JLabel("+");
		lbl.setBounds(106, 59, 57, 15);
		contentPane.add(lbl);
		
		JButton btnSum = new JButton("=");
		btnSum.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int first = Integer.parseInt(firstNum.getText());
				int second = Integer.parseInt(secondNum.getText());
				result.setText(Integer.toString(first+second));
			}
		});
		
		btnSum.setBounds(244, 55, 46, 23);
		contentPane.add(btnSum);
		
		result = new JTextField();
		result.setBounds(319, 56, 72, 21);
		contentPane.add(result);
		result.setColumns(10);
	}
}
