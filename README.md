# GCN-for-Human-Action-Recognition
- Nhận dạng hành động người là một nhiệm vụ quan trọng trong lĩnh vực thị giác máy tính. Trong công trình này chúng tôi tập trung vào việc nhận dạng hành động người dựa vào khung xương bằng việc áp dụng kiến trúc mạng tích chập đồ thị (GCN). 
- Công trình sử dụng ST-GCN (https://arxiv.org/abs/1801.07455) làm backbone và gắn thêm mô đun TAM được lấy ý tưởng từ bài viết (https://doi.org/10.1049/cvi2.12017). Ngoài ra công trình còn áp dụng một phương pháp chuẩn hóa khung xương, điều này có thể khiến mô hình bị quá khớp dữ liệu nhưng với một số hành động nhất định thì việc chuẩn hóa khung xương có hiệu quả khả quan.
- Dữ liệu: NTU RGB+D: contains 60 action classes
