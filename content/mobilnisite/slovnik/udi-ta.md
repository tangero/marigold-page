---
slug: "udi-ta"
url: "/mobilnisite/slovnik/udi-ta/"
type: "slovnik"
title: "UDI-TA – Unrestricted Digital Information with Tones/Announcements"
date: 2025-01-01
abbr: "UDI-TA"
fullName: "Unrestricted Digital Information with Tones/Announcements"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/udi-ta/"
summary: "Přenosová služba pro přenos digitálních dat spolu s tóny nebo hlášeními v pásmu. Podporuje aplikace jako faxová a modemová volání, kde musí být síťově generované zvukové signály prokládány s uživatels"
---

UDI-TA je okruhově přepínaná přenosová služba, která přenáší neomezená digitální data prokládaná síťově generovanými tóny nebo hlášeními v pásmu, primárně pro faxové a modemové aplikace.

## Popis

Služba Unrestricted Digital Information with Tones/Announcements (UDI-TA) je okruhově přepínaná přenosová služba standardizovaná organizací 3GPP. Je navržena pro přenos neomezených digitálních informací, což jsou v podstatě transparentní data, a zároveň umožňuje vkládání síťově generovaných tónů nebo hlášení v pásmu do datového toku. Tato schopnost je klíčová pro podporu starších nehlasových služeb, jako je fax skupiny 3 a pásmové datové modemy, přes digitální mobilní sítě. Tyto aplikace často vyžadují, aby síť během fáze sestavování hovoru nebo přenosu dat poskytovala specifické zvukové signály, jako jsou vyzváněcí tóny, obsazovací tóny nebo nahraná hlášení. UDI-TA zajišťuje, že tyto tóny jsou doručovány v pásmu, což znamená, že jsou smíchány s uživatelskými daty ve stejném 64 kbit/s časovém slotu, a tím je zachována kompatibilita s očekáváním koncového uživatelského zařízení.

Z architektonického hlediska je UDI-TA implementována v rámci jádra sítě (Core Network, CN), konkrétně se zapojením ústředny mobilního přepojování (Mobile Switching Centre, [MSC](/mobilnisite/slovnik/msc/)) a potenciálně bránové MSC (Gateway MSC, [GMSC](/mobilnisite/slovnik/gmsc/)) pro propojení s jinými sítěmi. Služba funguje v tradiční okruhově přepínané doméně. Když je UDI-TA hovor sestaven, MSC spravuje přenosovou cestu. Klíčovým funkčním aspektem je schopnost MSC generovat nebo získat požadované tóny/hlášení a multiplexovat je s datovým tokem uživatele pocházejícím z mobilní stanice nebo externí sítě. K tomuto multiplexování dochází na úrovni 64 kbit/s, čímž je zajištěno správné doručení složeného signálu příjemci.

Služba funguje na základě definice specifických schopností a atributů přenosu informací v rámci procedur řízení hovoru. Během sestavování hovoru síť indikuje použití přenosové služby UDI-TA. MSC je následně zodpovědná za transparentní přenos uživatelských dat a zároveň má schopnost v případě potřeby vložit zvukové signály. Například, pokud faxové volání narazí na obsazený cíl, může síť vložit obsazovací tón do datového toku odesílaného zpět k volající faxové stanici, což ji přiměje k odpovídající reakci. Technické specifikace, především TS 29.163, podrobně popisují požadavky na propojení mezi sítí 3GPP a jinými sítěmi (jako je [PSTN](/mobilnisite/slovnik/pstn/)/[ISDN](/mobilnisite/slovnik/isdn/)) pro podporu této služby, což zajišťuje bezproblémový provoz přes hranice sítí.

Úlohou UDI-TA je překlenout propast mezi plně digitálními mobilními sítěmi a datovými komunikačními zařízeními z analogové éry. Poskytuje standardizovanou metodu pro podporu těchto starších služeb bez nutnosti úprav koncového uživatelského zařízení. I když její význam poklesl s rozšířením paketově přepínaných datových služeb (jako je IP) a úpadkem okruhově přepínaných sítí, byla klíčovou součástí pro úplnost služeb v dřívějších vydáních 3GPP, zajišťujíc zpětnou kompatibilitu a širokou nabídku služeb během přechodu ze sítí 2G na 3G.

## K čemu slouží

UDI-TA byla vytvořena za účelem řešení problému podpory starších nehlasových telekomunikačních služeb, konkrétně faxové a modemové komunikace, přes digitální celulární sítě. V analogovém světě [PSTN](/mobilnisite/slovnik/pstn/) tyto služby spoléhaly na to, že síť poskytuje specifické zvukové tóny v pásmu (např. tón volby, obsazovací tón, vyzváněcí tón) a nahraná hlášení během hovoru. Jednoduchý transparentní digitální datový kanál by tyto síťově generované signály nepřenášel, což by způsobilo poruchu nebo úplné selhání staršího koncového zařízení.

Motivace pramenila z potřeby, aby sítě GSM a UMTS nabízely úplnou náhradu pevných linek, včetně obchodně kritických faxových a datových modemových spojení. Bez služby jako je UDI-TA by mobilní sítě nebyly schopny podporovat tyto rozšířené aplikace, což by omezilo jejich komerční atraktivitu a užitečnost. Tato technologie řešila omezení čisté přenosové služby Unrestricted Digital Information ([UDI](/mobilnisite/slovnik/udi/)), která byla pouze pro transparentní data, přidáním klíčové schopnosti sítě vkládat řídicí signály přímo do datového toku uživatele.

Historicky to byla klíčová vlastnost pro okruhově přepínané datové služby ([CSD](/mobilnisite/slovnik/csd/)) a vysokorychlostní okruhově přepínané datové služby ([HSCSD](/mobilnisite/slovnik/hscsd/)). Zajišťovala, že když zákazníci přecházeli z pevných na mobilní služby, jejich stávající faxové přístroje a modemy budou i nadále správně fungovat. Specifikace poskytla standardizované řešení pro propojení, které bylo nezbytné pro globální roaming a propojení s dalšími pevnými a mobilními sítěmi, které také potřebovaly podporovat tyto tóny a hlášení.

## Klíčové vlastnosti

- Transparentní přenos neomezených digitálních uživatelských dat (64 kbit/s)
- Vkládání síťově generovaných tónů v pásmu (např. tón volby, obsazovací, přetížení)
- Vkládání síťově generovaných nahraných hlášení v pásmu
- Podpora starších nehlasových služeb, jako je fax skupiny 3 a modemy řady V
- Definované postupy pro propojení se sítěmi PSTN/ISDN
- Okruhově přepínaná přenosová služba spravovaná MSC

## Související pojmy

- [UDI – Unrestricted Digital Interface](/mobilnisite/slovnik/udi/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [UDI-TA na 3GPP Explorer](https://3gpp-explorer.com/glossary/udi-ta/)
