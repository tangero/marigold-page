---
slug: "r2d"
url: "/mobilnisite/slovnik/r2d/"
type: "slovnik"
title: "R2D – Reader to Device"
date: 2026-01-01
abbr: "R2D"
fullName: "Reader to Device"
category: "IoT"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/r2d/"
summary: "R2D je komunikační režim definovaný v 3GPP pro celulární IoT, ve kterém připojené zařízení (Reader) iniciuje komunikaci s jednodušším, často energeticky omezeným zařízením (Device). Je klíčovým prvkem"
---

R2D je komunikační režim 3GPP pro celulární IoT, ve kterém připojený čtecí prvek (Reader) iniciuje komunikaci s jednodušším zařízením (Device) s omezenou kapacitou baterie, aby umožnil energeticky úsporné aplikace hromadného IoT.

## Popis

Reader to Device (R2D) je komunikační paradigma standardizované v rámci 3GPP Release 19, primárně pro hromadný internet věcí (IoT) a kritické IoT aplikace. Definuje síťovou architekturu a procedury, ve kterých celulárně připojená entita, označovaná jako Reader, iniciuje downlinkovou komunikaci směrem k velkému množství jednodušších koncových zařízení (Device). Tato zařízení jsou typicky senzory, tagy nebo aktuátory, která jsou extrémně omezená z hlediska výdrže baterie, složitosti a nákladů. Model R2D je základním kamenem pro efektivní sběr dat z rozsáhlých senzorových sítí a bezdrátové řízení.

Architektonicky je Reader síťově schopný uzel, který může být vyhrazenou bránou, uživatelským zařízením (UE), nebo dokonce síťovou funkcí v cloudu operátora. K 5G Core Network se připojuje pomocí standardních procedur UE. Koncová zařízení jsou však optimalizována pro minimální aktivitu. Nemusejí provádět pravidelné registrace, správu mobility ani trvale udržovat kontext v core síti. Místo toho zůstávají v hlubokém spánkovém stavu a probouzejí se pouze během předdefinovaných, sítí nakonfigurovaných oken, aby naslouchala pagingu nebo přímým datovým přenosům od Readeru přes 5G rádiovou přístupovou síť (NG-RAN). Komunikace je síťově asistovaná, což znamená, že core síť ([AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/)) pomáhá spravovat identity, zabezpečení a směrovací kontext pro zařízení, i když samotná zařízení mají velmi odlehčený protokolový stack.

Jak to funguje, zahrnuje několik klíčových procedur definovaných v uvedených specifikacích. Síť vysílá systémovou informaci konfigurující parametry specifické pro R2D. Zařízení se na ni synchronizují a vstoupí do cyklu přerušovaného příjmu ([DRX](/mobilnisite/slovnik/drx/)). Když má Reader data k odeslání (např. aktualizaci konfigurace nebo požadavek na odečet senzoru), odešle uplinkový požadavek do své obsluhující gNB s uvedením cílového zařízení nebo skupiny. Síť následně naplánuje downlinkový přenos v aktivním okně zařízení, případně s využitím skupinové signalizace. Zařízení data přijme, zpracuje je a může odeslat odpověď v následném uplinkovém prostředku přiděleném sítí. Tento model invertuje typické IoT paradigma, kde komunikaci iniciuje zařízení, což umožňuje zařízením ušetřit značné množství energie odstraněním potřeby periodických uplinkových přenosů pro udržení připojení k síti.

## K čemu slouží

R2D bylo vytvořeno, aby řešilo základní omezení stávajících celulárních IoT technologií (jako NB-IoT a LTE-M) pro extrémně rozsáhlá nasazení. Zatímco tyto technologie výborně umožňují zařízením odesílat data, jsou méně optimální pro scénáře, kde síť potřebuje *iniciovat* komunikaci s obrovským množstvím pasivních, bateriově omezených zařízení. Primárním problémem je spotřeba energie: požadavek, aby se zařízení periodicky probouzelo a naslouchalo pagingu nebo udržovalo síťovou registraci pro potenciální downlinkový provoz, vyčerpává jeho baterii.

Motivace vychází z nových případů užití IoT, jako jsou bezdrátové senzorové sítě, kde je třeba na požádání dotazovat tisíce environmentálních senzorů, nebo sledování aktiv, kde jsou aktualizace polohy vyžádány centrálním systémem pouze v případě potřeby. Předchozí přístupy buď spoléhaly na naplánované uplinkové přenosy (plýtvání energií, pokud nejsou data potřeba), nebo používaly necestulární technologie jako LoRa pro downlink, což vytvářelo integrační složitost. R2D to řeší architektonickým uzpůsobením 5G systému pro efektivní, síťově řízenou dominanci downlinku. Umožňuje zařízením být z pohledu core sítě virtuálně 'offline' až do chvíle, kdy jsou potřeba, což dramaticky prodlužuje výdrž baterie z let na potenciálně desetiletí. To umožňuje skutečně masivní měřítko IoT snížením signalizační režie a konkurence o rádiové prostředky pro uplinkově orientovaný provoz.

## Klíčové vlastnosti

- Síťově iniciovaná downlinková komunikace s masivním množstvím omezených zařízení
- Zařízení pracují s ultra-nízkou spotřebou energie pomocí rozšířeného DRX a minimální signalizace
- Podpora jak unicastového, tak groupcastového/multicastového doručování dat do skupin zařízení
- Síťově spravovaný kontext zařízení, což snižuje potřebný stav a zpracování na koncovém zařízení
- Integrováno s 5G NR, podpora provozu v kmitočtových pásmech FR1 a FR2
- Rozšířené bezpečnostní procedury pro autentizaci a ochranu transakcí R2D

## Definující specifikace

- **TS 33.369** (Rel-19) — Security for AIoT in Isolated Private 5G Networks
- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.194** (Rel-19) — Ambient IoT Base Station RF Spec
- **TS 38.291** (Rel-19) — Ambient IoT Physical Layer Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.391** (Rel-19) — NR; Ambient IoT MAC Protocol Spec
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR
- **TS 38.870** (Rel-19) — Enhanced OTA Test Methods for NR FR1 TRP/TRS

---

📖 **Anglický originál a plná specifikace:** [R2D na 3GPP Explorer](https://3gpp-explorer.com/glossary/r2d/)
