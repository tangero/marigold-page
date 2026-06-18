---
slug: "sl-mt-lr"
url: "/mobilnisite/slovnik/sl-mt-lr/"
type: "slovnik"
title: "SL-MT-LR – Sidelink Mobile Terminating Location Request"
date: 2025-01-01
abbr: "SL-MT-LR"
fullName: "Sidelink Mobile Terminating Location Request"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sl-mt-lr/"
summary: "Služba umožňující externí entitě nebo jinému UE vyžádat si polohu cílového UE prostřednictvím sidelink komunikace. Umožňuje sledování polohy ve scénářích komunikace přímo mezi zařízeními, což je klíčo"
---

SL-MT-LR je služba, při které externí entita nebo jiné UE vyžádá polohu cílového UE pomocí sidelink komunikace, což umožňuje sledování polohy zařízení přímo mezi zařízeními pro aplikace jako jsou sítě V2X.

## Popis

SL-MT-LR (Sidelink Mobile Terminating Location Request) je služba určování polohy v rámci standardů 3GPP, která umožňuje externí entitě, jako je lokační server nebo jiné UE, vyžádat si zeměpisnou polohu cílového UE pomocí sidelink komunikace. Na rozdíl od [SL-MO-LR](/mobilnisite/slovnik/sl-mo-lr/), kde žádost iniciuje UE, zde cílové UE přijímá žádost ukončenou z externího zdroje přes rozhraní PC5. Tato služba je zásadní pro scénáře, kdy třetí strana potřebuje zjistit polohu zařízení, například při zásazích záchranných složek, sledování vozidel nebo síťově asistovaném určování polohy. Postupy jsou podrobně popsány v specifikacích 23.273 pro architektonické aspekty, 24.514 pro protokolové vrstvy a 38.355 pro integraci s rádiovým přístupovým sítí, což zajišťuje standardizovaný přístup napříč různými nasazeními sítí.

Architektura pro SL-MT-LR zahrnuje několik klíčových komponent: žádající entitu, kterou může být UE nebo síťový lokační server; cílové UE, což je zařízení, jehož poloha je zjišťována; a rozhraní PC5, které zprostředkovává přímou sidelink komunikaci. Žádající entita odešle zprávu s žádostí o polohu přes rozhraní PC5, která obsahuje parametry jako identifikaci cílového UE, požadovanou přesnost a metodu určování polohy. Po přijetí cílové UE žádost zpracuje, což může zahrnovat aktivaci svých lokalizačních modulů, měření signálů, jako je [SL-PRS](/mobilnisite/slovnik/sl-prs/) od sousedních zařízení, nebo koordinaci s jinými UE pro kolaborativní určování polohy. Cílové UE následně vypočte nebo napomůže vypočítat svou polohu, často za použití technik jako měření doby příchodu nebo úhlu příchodu, a výsledek vrátí žádající entitě přes stejný sidelink kanál.

SL-MT-LR funguje prostřednictvím série signalizačních výměn definovaných v příslušných specifikacích 3GPP. Nejprve žádající entita sestaví zprávu s žádostí o polohu na základě potřeb aplikace – například ve scénáři [V2X](/mobilnisite/slovnik/v2x/) může vozovková jednotka vyžadovat polohu blízkých vozidel pro řízení provozu. Tato zpráva je přenášena přes [SL-SCH](/mobilnisite/slovnik/sl-sch/) (Sidelink Shared Channel) s využitím rozhraní PC5. Cílové UE po dekódování žádosti zahájí měřicí procedury, případně zahrnující výměnu referenčních signálů s jinými UE nebo infrastrukturou. Pokud cílové UE nemá dostatečné schopnosti, může žádost přeposlat lokačnímu serveru nebo použít hybridní metody kombinující sidelink a buněčná měření. Vypočtená polohová data jsou následně zapouzdřena do odpovědní zprávy a odeslána zpět přes PC5. Tato služba je navržena jako efektivní, s mechanismy pro ochranu soukromí a zabezpečení, jako je autentizace žádajících entit, aby se zabránilo neoprávněnému sledování. Její role v síti přesahuje pouhé určování polohy; umožňuje dynamické přidělování zdrojů a zvýšenou situační povědomost v sidelink ekosystémech, podporujíc vše od logistiky po zotavení z katastrof.

## K čemu slouží

SL-MT-LR byl vyvinut pro potřeby externích entit lokalizovat UE v sidelink prostředích, kde tradiční síťové služby ukončovaného určování polohy nejsou proveditelné. V aplikacích jako [V2X](/mobilnisite/slovnik/v2x/) a [ProSe](/mobilnisite/slovnik/prose/) často existuje požadavek, aby jedno zařízení nebo systém určil polohu jiného – například záchranné služby lokalizující vozidlo po nehodě nebo správce vozového parku sledující aktiva v odlehlých oblastech. Předchozí metody spoléhaly na účast buněčné sítě, která mohla selhat v oblastech bez pokrytí nebo při přetížení. SL-MT-LR umožňuje přímé, mezi zařízeními probíhající žádosti o polohu, čímž zlepšuje spolehlivost a snižuje latenci pro kritické operace.

Historicky byly služby Mobile Terminating Location Request ([MT-LR](/mobilnisite/slovnik/mt-lr/)) v 3GPP omezeny na interakce s jádrem sítě, vyžadující zprostředkování žádostí základnovou stanicí a prvky jádra sítě. S nástupem sidelink komunikace v releasách jako Rel-16 pro NR se tento přístup ukázal jako nedostatečný pro use case přímé komunikace. SL-MT-LR vznikl jako řešení, rozšiřující možnosti ukončovaného určování polohy na rozhraní PC5. To bylo motivováno požadavky automobilového průmyslu a sektoru veřejné bezpečnosti na robustní určování polohy pro kolaborativní povědomí, například v jízdě v koloně nebo pátracích a záchranných misích, kde zařízení musí sdílet polohová data bez síťové režie.

Vytvoření SL-MT-LR také podporuje regulatorní shodu a komerční aplikace, umožňující služby jako zákonné odposlechy nebo lokalizačně cílenou reklamu v sidelink kontextech. Jeho standardizací v 3GPP je zajištěna interoperabilita napříč různými zařízeními a sítěmi, což řeší fragmentaci pozorovanou u proprietárních řešení. Tento vývoj odráží širší trend směrem k decentralizovaným síťovým funkcím, umožňující zařízením provádět komplexní úlohy nezávisle při zachování bezproblémové integrace s existující buněčnou infrastrukturou.

## Klíčové vlastnosti

- Umožňuje externím entitám vyžádat si polohu UE přes sidelink rozhraní PC5
- Podporuje zpracování žádosti o polohu a odpověď cílového UE
- Integruje se s V2X a ProSe pro scénáře kolaborativního určování polohy
- Obsahuje mechanismy ochrany soukromí a zabezpečení pro autorizovaný přístup
- Využívá sidelink měření, jako je SL-PRS, pro přesné určování polohy
- Poskytuje odolnost v prostředích bez infrastruktury nebo v ad-hoc sítích

## Související pojmy

- [SL-MO-LR – Sidelink Mobile Originating Location Request](/mobilnisite/slovnik/sl-mo-lr/)
- [SL-PRS – Sidelink Positioning Reference Signals](/mobilnisite/slovnik/sl-prs/)
- [MT-LR – Mobile Terminated Location Request](/mobilnisite/slovnik/mt-lr/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 24.514** (Rel-19) — Ranging & Sidelink Positioning in 5GS
- **TS 38.355** (Rel-19) — Sidelink Positioning Protocol (SLPP)

---

📖 **Anglický originál a plná specifikace:** [SL-MT-LR na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-mt-lr/)
