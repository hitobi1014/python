package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.ImageIcon;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class FrmOmok01 extends JFrame {

	private JPanel contentPane;
	private JLabel[][] arr2d = new JLabel[10][10];
	private ImageIcon iie = new ImageIcon(FrmOmok01.class.getResource("/day04/0.jpg"));
	private ImageIcon iiw = new ImageIcon(FrmOmok01.class.getResource("/day04/1.jpg"));
	private ImageIcon iib = new ImageIcon(FrmOmok01.class.getResource("/day04/2.jpg"));
	
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					FrmOmok01 frame = new FrmOmok01();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	public FrmOmok01() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 750, 750);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		for(int i=0;i<arr2d.length;i++) {
			for(int j=0;j<arr2d[i].length;j++) {
				JLabel lbl = new JLabel("New label");
				lbl.setIcon(iie);
				lbl.setText(i+","+j);
				lbl.setBounds(75*i, 75*j, 75, 75);
				arr2d[i][j]=lbl;
				lbl.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						JLabel temp = (JLabel) e.getComponent();
						System.out.println(temp.getText());
//						if(toggle==1) {
//							lbl.setIcon(iiw);
//							toggle=0;
//						}else {
//							lbl.setIcon(iib);
//							toggle=1;
//						}
					}
				});
				contentPane.add(lbl);
				arr2d[i][j]=lbl;
			}
		}
		
	}
	
	
	
}
