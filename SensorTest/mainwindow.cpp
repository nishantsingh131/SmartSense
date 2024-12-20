#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QSerialPortInfo>
#include <QDebug>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow) {
    ui->setupUi(this);

    // Initialize the serial port
    serial = new QSerialPort(this);

    // Configure serial port settings
    serial->setPortName("COM3"); // Replace with your Arduino COM port
    serial->setBaudRate(QSerialPort::Baud9600);
    serial->setDataBits(QSerialPort::Data8);
    serial->setParity(QSerialPort::NoParity);
    serial->setStopBits(QSerialPort::OneStop);
    serial->setFlowControl(QSerialPort::NoFlowControl);

    // Open the serial port
    if (!serial->open(QIODevice::ReadOnly)) {
        qDebug() << "Failed to open port";
        ui->textEdit->setText("Error: Unable to connect to Arduino");
        return;
    }

    // Connect readyRead signal to readSerialData slot
    connect(serial, &QSerialPort::readyRead, this, &MainWindow::readSerialData);
}

void MainWindow::readSerialData() {
    while (serial->canReadLine()) {
        QByteArray data = serial->readLine();
        QStringList values = QString(data).split(',');

        if (values.size() >= 2) {
            ui->textEdit->setText(values[0].trimmed());   // Temperature
            ui->textEdit_2->setText(values[1].trimmed()); // Humidity
        }
    }
}

MainWindow::~MainWindow() {
    if (serial->isOpen()) {
        serial->close();
    }
    delete ui;

}
