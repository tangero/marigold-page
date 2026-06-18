---
slug: "guk-id"
url: "/mobilnisite/slovnik/guk-id/"
type: "slovnik"
title: "GUK-ID – Group User Key Identifier"
date: 2026-01-01
abbr: "GUK-ID"
fullName: "Group User Key Identifier"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/guk-id/"
summary: "Jedinečný identifikátor pro skupinový uživatelský klíč (GUK) používaný v službách 3GPP založených na blízkosti (ProSe). Umožňuje bezpečnou skupinovou komunikaci a vyhledávání mezi zařízeními tím, že i"
---

GUK-ID je jedinečný identifikátor pro skupinový uživatelský klíč (Group User Key) používaný v 3GPP ProSe k zajištění bezpečné skupinové komunikace a vyhledávání tím, že identifikuje konkrétní kryptografický klíč sdílený definovanou skupinou uživatelů.

## Popis

Identifikátor skupinového uživatelského klíče (GUK-ID) je klíčový bezpečnostní parametr v architektuře 3GPP pro služby založené na blízkosti ([ProSe](/mobilnisite/slovnik/prose/)), které umožňují komunikaci typu zařízení-zařízení ([D2D](/mobilnisite/slovnik/d2d/)). Slouží jako jedinečná značka nebo odkaz na konkrétní skupinový uživatelský klíč (GUK), což je symetrický kryptografický klíč sdílený všemi členy skupiny ProSe. Samotný GUK se používá k zabezpečení skupinové komunikace, například k šifrování a ochraně integrity provozu odesílaného mezi členy skupiny přes přímé rozhraní PC5 nebo přes síťový přenos. GUK-ID neobsahuje samotný klíčový materiál; jedná se o ne-tajný identifikátor, který umožňuje zařízením a síťovým funkcím jednoznačně odkazovat na správný GUK a načíst jej ze svého zabezpečeného úložiště (např. UICC nebo důvěryhodného prostředí pro provádění) při potřebě kryptografických operací.

Z architektonického hlediska je GUK-ID spolu s odpovídajícím GUK zajišťován autorizovaným uživatelským zařízením (User Equipment, UE) funkcí ProSe v síti, jak je definováno ve specifikacích jako TS 23.303 a bezpečnostních specifikacích TS 33.179 a 33.180. Samotný proces zajištění je zabezpečen. Když se UE chce zapojit do bezpečné skupinové komunikace nebo vyhledávání, zahrne příslušný GUK-ID do signalizačních zpráv. Ostatní UE ve skupině po přijetí tohoto identifikátoru jej mohou použít k nalezení stejného GUK ve své lokální paměti a dešifrovat tak zprávy nebo ověřit kontrolní součty integrity. Funkce ProSe také používá GUK-ID ke správě životního cyklu skupinových klíčů, včetně jejich aktualizací, odvolání a změn členství. Identifikátor je strukturován tak, aby byl v kontextu vydávající funkce ProSe nebo širší domény globálně jedinečný, aby se předešlo kolizím.

Jeho role je zásadní pro škálovatelnou a bezpečnou správu skupin v ProSe. Bez stručného identifikátoru by zařízení musela vyměňovat nebo odkazovat na celou hodnotu klíče, což je nebezpečné a neefektivní. GUK-ID umožňuje efektivní indexování a vyhledávání klíčů. Používá se v různých postupech ProSe: při přímém vyhledávání může UE vysílat zprávu podepsanou klíčem asociovaným s GUK-ID, aby prokázala své členství ve skupině; při skupinové komunikaci jeden-všem odesílající UE zašifruje data pomocí GUK a přijímače použijí signalizovaný GUK-ID k výběru správného dešifrovacího klíče. Tento mechanismus je zásadní pro scénáře veřejné bezpečnosti, kde záchranáři vytvářejí dynamické skupiny, stejně jako pro komerční aplikace, jako je sociální síťování založené na poloze. Bezpečnostní specifikace podrobně popisují, jak je GUK-ID vázán na omezení použití GUK a metadata skupiny, což zajišťuje, že identifikátor nemůže být zneužit k odvození klíčového materiálu nebo k vydávání se za skupinu bez vlastnictví skutečného klíče.

## K čemu slouží

GUK-ID byl vytvořen k řešení specifických bezpečnostních a škálovatelných výzev skupinové komunikace typu zařízení-zařízení zavedené se službami založenými na blízkosti ([ProSe](/mobilnisite/slovnik/prose/)) ve 3GPP Release 12 a dále vylepšené. Před ProSe se bezpečnost v celulárních sítích zaměřovala primárně na zabezpečení typu bod-bod mezi jednotlivým UE a sítí (např. pomocí KASME v LTE). ProSe zavedlo scénáře, kde zařízení potřebují komunikovat přímo bezpečným, skupinově orientovaným způsobem, zejména pro veřejnou bezpečnost, kde musí být rychle vytvořeny ad-hoc skupiny záchranářů. Základním problémem bylo, jak efektivně a bezpečně spravovat sdílené kryptografické klíče pro potenciálně mnoho dynamických skupin. Pouhé použití hodnoty klíče jako identifikátoru je bezpečnostní anti-pattern. GUK-ID poskytuje mechanismus nepřímého odkazování, který to řeší tím, že umožňuje bezpečnou signalizaci o tom, který klíč použít, aniž by byl klíč sám odhalen.

Historická motivace vychází z potřeby systémů komunikace pro klíčové mise, které mohou fungovat částečně nebo plně bez síťové infrastruktury (mimo dosah sítě). V takových scénářích musí být zařízení schopna se vzájemně autentizovat a autonomně vytvářet zabezpečené kanály. GUK, identifikovaný pomocí GUK-ID, je předem sdílen prostřednictvím sítě, když je dostupná, což umožňuje toto zabezpečení mimo síť. Mechanismus GUK-ID řeší problém identifikace klíčů v signalizaci s omezenými prostředky. Umožňuje zařízení signalizovat: "pro tuto relaci použij skupinový klíč, který oba známe pod 'ID-12345'", čímž je protokol lehký. Dále umožňuje efektivní obnovu klíčů; když je GUK aktualizován, je vydáno nové GUK-ID a zařízení mohou plynule přejít na nový klíč, zatímco starý klíč odkazovaný starým ID je zahozen. To je zásadní pro zachování dopředné důvěrnosti a správu kompromitovaných zařízení ve skupině. Bez takového identifikátoru by byla správa skupinových klíčů těžkopádná, náchylná k chybám a méně bezpečná, což by bránilo přijetí ProSe pro kritické služby.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor pro konkrétní skupinový uživatelský klíč (GUK)
- Umožňuje bezpečné a efektivní odkazování na kryptografické klíče v signalizaci
- Používá se v postupech přímého vyhledávání a skupinové komunikace ProSe
- Zajišťován funkcí ProSe spolu s GUK
- Usnadňuje správu životního cyklu skupinových klíčů (aktualizace, odvolání)
- Zásadní pro bezpečný provoz D2D jak v síťové pokrytí, tak i mimo něj

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.581** (Rel-19) — MCVideo Media Plane Control Protocol Specification
- **TS 29.380** (Rel-19) — MCPTT-LMR Interworking Media Plane Control
- **TS 29.582** (Rel-19) — MCData Interworking with LMR Systems
- **TS 33.179** (Rel-13) — MCPTT Security Architecture and Procedures
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.879** (Rel-13) — MCPTT Security Study

---

📖 **Anglický originál a plná specifikace:** [GUK-ID na 3GPP Explorer](https://3gpp-explorer.com/glossary/guk-id/)
