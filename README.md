1. Скопировать userdir.service в /lib/systemd/system
2. Скопировать userdir.timer в /lib/systemd/system
3. Изменить путь к python и скрипту в userdir.service

4. Перечитать конфигурацию systemd
`systemctl daemon-reload`

5. Создаем симлинку для автоматического запуска после перезагрузки
`systemctl enable userdir.timer`
Отобразиться (Created symlink /etc/systemd/system/timers.target.wants/userdir.timer → /lib/systemd/system/userdir.timer.)

6. Запустить
`systemctl start userdir.timer`
