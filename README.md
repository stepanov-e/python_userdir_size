1. Скопирвать userdir.service в /lib/systemd/system
2. Скопирвать userdir.timer в /lib/systemd/system

3. Перечитать конфигурацию systemd
`systemctl daemon-reload`

4. Создаем симлинку для автоматического запуска после перезагрузки
`systemctl enable userdir.timer`
Отобразиться (Created symlink /etc/systemd/system/timers.target.wants/userdir.timer → /lib/systemd/system/userdir.timer.)

5. Запускаем
`systemctl start userdir.timer`
