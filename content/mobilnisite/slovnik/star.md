---
slug: "star"
url: "/mobilnisite/slovnik/star/"
type: "slovnik"
title: "STAR – Short Term Automatically Renewed"
date: 2025-01-01
abbr: "STAR"
fullName: "Short Term Automatically Renewed"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/star/"
summary: "STAR je bezpečnostní mechanismus pro automatické obnovování krátkodobých přihlašovacích údajů, jako jsou certifikáty nebo klíče, bez manuálního zásahu. Je klíčový pro udržení nepřetržitého zabezpečení"
---

STAR je bezpečnostní mechanismus pro automatické obnovování krátkodobých přihlašovacích údajů za účelem zachování nepřetržitého zabezpečení bez manuálního zásahu, zejména pro IoT zařízení a dynamické síťové funkce.

## Popis

Short Term Automatically Renewed (STAR) je rámec definovaný ve specifikacích 3GPP pro automatické obnovování bezpečnostních přihlašovacích údajů s omezenou dobou platnosti. Funguje v rámci bezpečnostní architektury pro správu životního cyklu certifikátů nebo klíčů používaných uživatelským zařízením (UE), síťovými funkcemi nebo IoT zařízeními. Proces typicky zahrnuje entitu pro správu přihlašovacích údajů, jako je certifikační autorita ([CA](/mobilnisite/slovnik/ca/)) nebo server pro správu klíčů, která vydá počáteční přihlašovací údaje s krátkou dobou platnosti. Před vypršením platnosti entita vlastnící přihlašovací údaje iniciuje prostřednictvím zabezpečeného standardizovaného protokolu žádost o obnovení. Entita pro správu žádost ověří, často s využitím stávajících mechanismů ověřování a autorizace, a vydá nové přihlašovací údaje. Tyto nové přihlašovací údaje mohou mít aktualizované parametry nebo stejnou dobu platnosti, čímž se efektivně vytvoří posuvné okno důvěry bez přerušení služby.

Architektura podporující STAR je integrována se stávajícími bezpečnostními infrastrukturami 3GPP, jako je Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) a Security Edge Protection Proxy ([SEPP](/mobilnisite/slovnik/sepp/)) pro systémy 5G, nebo podobnými entitami v dřívějších vydáních. Mezi klíčové komponenty patří žadatel o přihlašovací údaje (např. UE nebo síťová funkce), vystavovatel přihlašovacích údajů (např. CA) a obsluha protokolu pro obnovení, která umožňuje automatizovanou výměnu. Protokol pro obnovení je navržen jako lehký a efektivní, aby minimalizoval signalizační režii, což je zvláště důležité pro IoT zařízení s omezenou kapacitou baterie. Často využívá mechanismy jako předautorizační tokeny nebo politiky obnovení založené na předplatném, aby zjednodušil proces.

Úloha STAR v síti spočívá v posílení bezpečnostní pozice omezením doby expozice jakéhokoli jednotlivého přihlašovacího údaje, čímž se zmírňují rizika spojená s jeho kompromitací. Automatizací obnovení odstraňuje potřebu manuálního opětovného zřizování, které je náchylné k chybám a neškálovatelné ve velkých nasazeních, jako je massive IoT. Rámec zajišťuje, že služby závislé na těchto přihlašovacích údajích, jako jsou zabezpečené komunikační kanály nebo přístupová autentizace, zůstávají nepřerušené. Jedná se o základní prvek pro zero-touch zřizování a autonomní správu síťové bezpečnosti v se vyvíjejících systémech 3GPP.

## K čemu slouží

STAR byl vytvořen, aby řešil výzvy spojené se správou krátkodobých bezpečnostních přihlašovacích údajů v moderních telekomunikačních sítích, zejména s rozšířením IoT zařízení a cloud-nativních síťových funkcí. Tradiční dlouhodobé certifikáty nebo statické klíče představují významná bezpečnostní rizika; pokud jsou kompromitovány, zůstávají platné po dlouhou dobu, což umožňuje dlouhodobé útoky. Manuální procesy obnovení jsou pro miliony zařízení nepraktické, což vede k potenciálním výpadkům služeb nebo bezpečnostním mezerám. STAR tuto obnovu automatizuje a umožňuje častou rotaci přihlašovacích údajů bez lidského zásahu, což je v souladu s osvědčenými postupy zabezpečení pro minimalizaci útočné plochy.

Historický kontext vychází z potřeby agilního zabezpečení v 5G a dalších generacích, kde síťové řezy, edge computing a dynamická nasazení služeb vyžadují robustní, automatizovanou správu identit. Předchozí přístupy spoléhaly na manuální nebo poloautomatizované metody, které nebyly škálovatelné nebo nesplňovaly požadavky na nízkou latenci nových služeb. STAR tato omezení řeší tím, že poskytuje standardizovaný, protokolem řízený mechanismus, který se hladce integruje s architekturami 3GPP. Podporuje regulatorní požadavky na silné ověřování a důvěrnost v kritických komunikacích, čímž zajišťuje, že se sítě mohou přizpůsobovat vyvíjejícím se hrozbám při zachování provozní efektivity.

## Klíčové vlastnosti

- Automatické obnovování krátkodobých přihlašovacích údajů bez manuálního zásahu
- Integrace s bezpečnostními entitami 3GPP, jako jsou AUSF a SEPP
- Lehký návrh protokolu vhodný pro IoT zařízení s omezenými zdroji
- Podpora správy životního cyklu certifikátů a klíčů
- Mechanismy předautorizace pro zjednodušení žádostí o obnovení
- Nepřetržitá dostupnost služeb díky prevenci výpadků způsobených vypršením platnosti přihlašovacích údajů

## Související pojmy

- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [SEPP – Security Edge Protection Proxy](/mobilnisite/slovnik/sepp/)

## Definující specifikace

- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TR 33.876** (Rel-18) — Technical Report on Certificate Management

---

📖 **Anglický originál a plná specifikace:** [STAR na 3GPP Explorer](https://3gpp-explorer.com/glossary/star/)
