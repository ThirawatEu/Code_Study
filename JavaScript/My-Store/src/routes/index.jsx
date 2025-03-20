import { useRoutes } from 'react-router-dom';

import AdminRoutes from './AdminRoutes';
import MainRoutes from './MainRoutes';

export default function ConfigRoutes() {
    let login = localStorage.getItem("isLogin");

    let routes = login ? AdminRoutes : MainRoutes; // ใช้ routes เป็น array ได้เลย

    return useRoutes(routes); // useRoutes ต้องใช้ array
}
