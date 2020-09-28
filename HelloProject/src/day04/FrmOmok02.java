package day04;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

public class FrmOmok02 extends JFrame {

	private JPanel contentPane;
	private JLabel[][] arr2d = new JLabel[10][10];
	private int[][] int2d = new int[10][10];
	private ImageIcon iie = new ImageIcon(FrmOmok02.class.getResource("/day04/0.jpg"));
	private ImageIcon iiw = new ImageIcon(FrmOmok02.class.getResource("/day04/1.jpg"));
	private ImageIcon iib = new ImageIcon(FrmOmok02.class.getResource("/day04/2.jpg"));
	private boolean flagTurn = true;
	private boolean flagIng = true;
	
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					FrmOmok02 frame = new FrmOmok02();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}
	
	public void myrender() {
		for(int i=0;i<int2d.length;i++) {
			for(int j=0;j<int2d[i].length;j++) {
				if(int2d[i][j]==0) {
					arr2d[i][j].setIcon(iie);
				}else if(int2d[i][j]==1) {
					arr2d[i][j].setIcon(iiw);
				}else if(int2d[i][j]==2) {
					arr2d[i][j].setIcon(iib);
				}
			}
		}
	}

	public FrmOmok02() {
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
				lbl.setBounds(75*j, 75*i, 75, 75);
				arr2d[i][j]=lbl;
				lbl.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						myclick(e);
					}
				});
				contentPane.add(lbl);
				arr2d[i][j]=lbl;
			}
		}
	}
	
	public void myclick(MouseEvent e) {
		if(!flagIng) {
			return;
		}
		JLabel temp = (JLabel) e.getComponent();
		String a = temp.getText();
		String[] strArr = a.split(",");
		int ii = Integer.parseInt(strArr[0]);
		int jj = Integer.parseInt(strArr[1]);
		if(int2d[ii][jj]>0) {
			return;
		}
		int cnt_stone = 1;
		if(flagTurn) {
			int2d[ii][jj]=1;
			cnt_stone = 1;
		}else if(!flagTurn){
			int2d[ii][jj]=2;
			cnt_stone = 2;
		}
		myrender();
		int up_cnt = getUp(ii,jj,cnt_stone);
		int dw_cnt = getDown(ii,jj,cnt_stone);
		int left_cnt = getleft(ii,jj,cnt_stone);
		int right_cnt = getright(ii,jj,cnt_stone);
		int upLe_cnt = getUpLe(ii,jj,cnt_stone);
		int upRi_cnt = getUpRi(ii,jj,cnt_stone);
		int dwLe_cnt = getDwLe(ii,jj,cnt_stone);
		int dwRi_cnt = getDwRi(ii,jj,cnt_stone);
		
		int[] cnt5p= new int[4];
		cnt5p[0] = up_cnt + dw_cnt + 1;
		cnt5p[1] = left_cnt + right_cnt + 1;
		cnt5p[2] = upLe_cnt + dwRi_cnt + 1;
		cnt5p[3] = upRi_cnt + dwLe_cnt + 1;
		for(int i=0;i<cnt5p.length;i++) {
			if(cnt5p[i]==5) {
				if(flagTurn) {
					// alert와 비슷한 기능
					JOptionPane.showMessageDialog(null, "흰돌이 이겼습니다");
				}else {
					JOptionPane.showMessageDialog(null, "흑돌이 이겼습니다");
				}
				flagIng = false;
			}
		}
//		System.out.println("up_cnt : " + up_cnt);
//		System.out.println("dw_cnt : " + dw_cnt);
//		System.out.println("left_cnt : " + left_cnt);
//		System.out.println("right_cnt : " + right_cnt);
//		
//		System.out.println("upLe_cnt: " + upLe_cnt);
//		System.out.println("upRi_cnt: " + upRi_cnt);
//		System.out.println("dwLe_cnt: " + dwLe_cnt);
//		System.out.println("dwRi_cnt: " + dwRi_cnt);
		flagTurn = !flagTurn;
	}
	
	public int getDwRi(int ii, int jj, int cnt_stone) {
		int cnt = 0;
		try {
			while(true) {
				ii++;
				jj++;
				if(int2d[ii][jj] == cnt_stone) {
					cnt++;
				}else {
					break;
				}
			}
		} catch (Exception e) {
			System.out.println("line out");
		}
		return cnt;
	}

	public int getDwLe(int ii, int jj, int cnt_stone) {
		int cnt = 0;
		try {
			while(true) {
				ii++;
				jj--;
				if(int2d[ii][jj] == cnt_stone) {
					cnt++;
				}else {
					break;
				}
			}
		} catch (Exception e) {
			System.out.println("line out");
		}
		return cnt;
	}
	
	public int getUpRi(int ii, int jj, int cnt_stone) {
		int cnt = 0; 
		try {
			while(true) {
				ii--;
				jj++;
				if(int2d[ii][jj] == cnt_stone) {
					cnt++;
				}else {
					break;
				}
			}
		} catch (Exception e) {
			System.out.println("line out");
		}
		return cnt;
	}
	
	public int getUpLe(int ii, int jj, int cnt_stone) {
		int cnt = 0; 
		try {
			while(true) {
				ii--;
				jj--;
				if(int2d[ii][jj] == cnt_stone) {
					cnt++;
				}else {
					break;
				}
			}
		} catch (Exception e) {
			System.out.println("line out");
		}
		return cnt;
	}
	
	public int getleft(int ii, int jj, int cnt_stone) {
		int cnt = 0;
		try {
			while(true) {
				jj--;
				if(int2d[ii][jj] == cnt_stone) {
					cnt++;
				}else {
					break;
				}
			}
		} catch (Exception e) {
			System.out.println("line out");
		}
		return cnt;
	}
	
	public int getright(int ii, int jj, int cnt_stone) {
		int cnt = 0;
		try {
			while(true) {
				jj++;
				if(int2d[ii][jj] == cnt_stone) {
					cnt++;
				}else {
					break;
				}
			}
		} catch (Exception e) {
			System.out.println("line out");
		}
		return cnt;
	}
	
	public int getDown(int ii, int jj, int cnt_stone) {
		int cnt = 0;
		try {
			while(true) {
				ii++;
				if(int2d[ii][jj] == cnt_stone) {
					cnt++;
				}else {
					break;
				}
			}
		} catch (Exception e) {
			System.out.println("line out");
		}
		return cnt;
	}
	
	public int getUp(int ii, int jj, int cnt_stone) {
		int cnt = 0; // 내 위로 같은 돌이 몇개있는지 알려줌
		// 무한루프....
		try {
			while(true) {
				ii--;
				if(int2d[ii][jj] == cnt_stone) {
					cnt++;
				}else {
					break;
				}
			}
		} catch (Exception e) {
			System.out.println("line out");
		}
		return cnt;
	}
}
