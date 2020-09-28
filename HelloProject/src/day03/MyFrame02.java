package day03;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

public class MyFrame02 extends JFrame {

	private JPanel contentPane;
	private JLabel lbl;
	int cnt=1;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame02 frame = new MyFrame02();
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
	public MyFrame02() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		String val = Integer.toString(cnt);
		lbl = new JLabel(val);
		lbl.setBounds(64, 44, 35, 15);
		contentPane.add(lbl);
		
		JButton btnIncrease = new JButton("증가");
		btnIncrease.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				cnt++;
				String to = Integer.toString(cnt);
				lbl.setText(to);
			}
		});
		btnIncrease.setBounds(226, 40, 97, 23);
		contentPane.add(btnIncrease);
	}

}
