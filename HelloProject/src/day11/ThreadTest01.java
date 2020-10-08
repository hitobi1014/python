package day11;

public class ThreadTest01 {
	public static void main(String[] args) {
		
		new Thread() {
			@Override
			public void run() {
				try {
					Thread.sleep(2000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
					System.out.println("hello");
			}
		}.start();
		
	}
	
}
