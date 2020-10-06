package day09;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JButton;
import java.awt.Color;
import javax.swing.JTable;
import javax.swing.JLabel;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class Tetris01 extends JFrame {

	private JPanel contentPane;
	private JTable table;
	private JLabel lbl ;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Tetris01 frame = new Tetris01();
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
	public Tetris01() {
		addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {
				int keycode = e.getKeyCode();
				// 위 38 왼쪽 37 오른쪽 39 아래 40
				int x = (int) lbl.getBounds().getX();
				int y = (int) lbl.getBounds().getY();
				int w = (int) lbl.getBounds().getWidth();
				int h = (int) lbl.getBounds().getHeight();
				if(keycode == 38) {lbl.setBounds(x, y-25, w, h);}
				if(keycode == 40) {lbl.setBounds(x, y+25, w, h);}
				if(keycode == 37) {lbl.setBounds(x-25, y, w, h);}
				if(keycode == 39) {lbl.setBounds(x+25, y, w, h);}
			}
		});
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 530, 559);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl = new JLabel("");
		lbl.setBackground(new Color(255, 140, 0));
		lbl.setBounds(84, 96, 25, 25);
		lbl.setOpaque(true);
		
		contentPane.add(lbl);
	}
}
