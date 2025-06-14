import { useTranslation } from 'react-i18next';

export default function LangSwitcher() {
  const { i18n } = useTranslation();
  const changeLang = (lng: string) => {
    i18n.changeLanguage(lng);
    const url = new URL(window.location.href);
    url.searchParams.set('lang', lng);
    window.history.replaceState(null, '', url.toString());
  };
  return (
    <select
      className="select select-bordered"
      value={i18n.language}
      onChange={(e) => changeLang(e.target.value)}
    >
      <option value="en">English</option>
      <option value="zh-CN">中文</option>
    </select>
  );
}
