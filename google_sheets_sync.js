/**
 * ==============================================================================
 * MEMOUR STUDIO - GOOGLE SHEETS AUTOMATIC SYNC SCRIPT
 * ==============================================================================
 * Bảng tính kết nối: email marketing (ID: 1sPPh_AWewPjGrpdxnBQYqHZghs3TVyBhaBEG3vso6Js)
 * Link: https://docs.google.com/spreadsheets/d/1sPPh_AWewPjGrpdxnBQYqHZghs3TVyBhaBEG3vso6Js/edit
 * 
 * HƯỚNG DẪN CÀI ĐẶT NHANH (Chỉ mất 1 phút):
 * 1. Mở link Google Sheet trên.
 * 2. Trên thanh menu, chọn: Tiện ích mở rộng (Extensions) -> Apps Script.
 * 3. Xóa hết code mặc định trong trình chỉnh sửa, copy và dán toàn bộ file code này vào.
 * 4. Bấm biểu tượng 💾 "Lưu dự án" (Save project).
 * 5. Bấm nút màu xanh "Triển khai" (Deploy) -> chọn "Quản lý bản triển khai mới" (New deployment).
 * 6. Mục "Chọn loại" (Select type) -> chọn "Ứng dụng web" (Web app).
 *    - Mô tả: "MEMOUR Contact Sync"
 *    - Thực thi dưới dạng (Execute as): "Tôi" (Me)
 *    - Ai có quyền truy cập (Who has access): "Bất kỳ ai" (Anyone)
 * 7. Bấm "Triển khai" (Deploy) và cấp quyền (Authorize access) cho tài khoản Google của bạn.
 * 8. Copy "URL ứng dụng web" (Web app URL có dạng: https://script.google.com/macros/s/.../exec).
 * ==============================================================================
 */

// Tên trang tính mặc định nhận thông tin
var SHEET_NAME = "Khách Hàng Kết Nối";

function setupSheetHeaders(sheet) {
  var headers = [
    "Thời Gian Gửi",
    "Họ Và Tên",
    "Số Điện Thoại / Zalo",
    "Email",
    "Lời Nhắn / Ý Tưởng Hợp Tác",
    "Trang Nguồn Tiếp Nhận",
    "Trạng Thái Xử Lý"
  ];
  
  sheet.appendRow(headers);
  
  // Định dạng tiêu đề đẹp mắt theo nhận diện MEMOUR Studio
  var headerRange = sheet.getRange(1, 1, 1, headers.length);
  headerRange.setFontWeight("bold");
  headerRange.setFontColor("#ffffff");
  headerRange.setBackground("#881337"); // Màu đỏ thương hiệu MEMOUR
  headerRange.setHorizontalAlignment("center");
  headerRange.setVerticalAlignment("middle");
  sheet.setRowHeight(1, 38);
  sheet.setFrozenRows(1);
  
  // Cài đặt độ rộng cột chuẩn để dễ đọc
  sheet.setColumnWidth(1, 170); // Thời gian
  sheet.setColumnWidth(2, 180); // Họ tên
  sheet.setColumnWidth(3, 160); // SĐT / Zalo
  sheet.setColumnWidth(4, 220); // Email
  sheet.setColumnWidth(5, 380); // Lời nhắn
  sheet.setColumnWidth(6, 200); // Nguồn
  sheet.setColumnWidth(7, 140); // Trạng thái
}

function getTargetSheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    // Nếu chưa có tab, lấy sheet đầu tiên và đổi tên hoặc tạo mới
    sheet = ss.getSheets()[0];
    try {
      sheet.setName(SHEET_NAME);
    } catch(e) {}
  }
  
  if (sheet.getLastRow() === 0) {
    setupSheetHeaders(sheet);
  }
  return sheet;
}

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(10000); // Khóa tránh xung đột khi nhiều người gửi cùng lúc
  
  try {
    var sheet = getTargetSheet();
    var data = {};
    
    if (e && e.postData && e.postData.contents) {
      try {
        data = JSON.parse(e.postData.contents);
      } catch (jsonErr) {
        data = e.parameter || {};
      }
    } else if (e && e.parameter) {
      data = e.parameter;
    }
    
    // Chuẩn bị dữ liệu từng cột
    var createdAt = data.created_at || Utilities.formatDate(new Date(), "Asia/Ho_Chi_Minh", "dd/MM/yyyy HH:mm:ss");
    var name = (data.name || "").toString().trim();
    var phone = (data.phone || "").toString().trim();
    var email = (data.email || "").toString().trim();
    var message = (data.message || "").toString().trim();
    if (data.subject && data.subject !== "") {
      message = "[" + data.subject + "] " + message;
    }
    var source = (data.source || "Website MEMOUR Studio").toString().trim();
    var status = "Mới tiếp nhận ✨";
    
    // Thêm dòng mới vào Google Sheet
    sheet.appendRow([
      createdAt,
      name,
      phone,
      email,
      message,
      source,
      status
    ]);
    
    // Canh lề dữ liệu mới thêm
    var lastRow = sheet.getLastRow();
    sheet.getRange(lastRow, 1).setHorizontalAlignment("center");
    sheet.getRange(lastRow, 3).setHorizontalAlignment("center");
    sheet.getRange(lastRow, 7).setHorizontalAlignment("center");
    sheet.getRange(lastRow, 7).setBackground("#fef9c3"); // Highlight vàng nhẹ trạng thái mới
    
    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      message: "Đã ghi nhận thông tin vào Google Sheet MEMOUR thành công!",
      row: lastRow
    })).setMimeType(ContentService.MimeType.JSON);
    
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: err.toString()
    })).setMimeType(ContentService.MimeType.JSON);
    
  } finally {
    lock.releaseLock();
  }
}

// Hàm test kết nối trực tiếp trên trình duyệt
function doGet(e) {
  return ContentService.createTextOutput(JSON.stringify({
    status: "active",
    name: "MEMOUR Studio Google Sheet Sync API",
    spreadsheetId: SpreadsheetApp.getActiveSpreadsheet().getId(),
    note: "API sẵn sàng tiếp nhận dữ liệu từ form Kết Nối Cùng MEMOUR Studio!"
  })).setMimeType(ContentService.MimeType.JSON);
}
