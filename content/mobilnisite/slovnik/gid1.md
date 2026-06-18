---
slug: "gid1"
url: "/mobilnisite/slovnik/gid1/"
type: "slovnik"
title: "GID1 – Group Identifier (level 1)"
date: 2025-01-01
abbr: "GID1"
fullName: "Group Identifier (level 1)"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gid1/"
summary: "GID1 je identifikátor souboru uložený na kartě USIM/UICC, definovaný v elementárním souboru EF(GID1). Síť jej používá k identifikaci skupiny nebo kategorie účastníků, často za účelem aplikace konkrétn"
---

GID1 je identifikátor souboru uložený na kartě USIM/UICC, který síť používá k identifikaci skupiny účastníků za účelem aplikace konkrétních služeb, přístupových omezení nebo komerčních nabídek.

## Popis

Group Identifier level 1 (GID1) je standardizovaný identifikátor v architektuře aplikace UICC (Universal Integrated Circuit Card) a [USIM](/mobilnisite/slovnik/usim/) (Universal Subscriber Identity Module) dle 3GPP. Je uložen jako datový objekt ve vyhrazeném elementárním souboru na kartě, konkrétně v [EF](/mobilnisite/slovnik/ef/)(GID1). Tento soubor je součástí souborového systému USIM, který je hierarchicky uspořádán pod vyhrazeným souborem aplikace USIM ([ADF](/mobilnisite/slovnik/adf/)). Hodnota GID1 je identifikátor poskytnutý sítí, což znamená, že je typicky zapsána na UICC mobilním operátorem ([MNO](/mobilnisite/slovnik/mno/)) během personalizace nebo prostřednictvím provizionování over-the-air ([OTA](/mobilnisite/slovnik/ota/)).

Technicky je EF(GID1) transparentní elementární soubor s pevnou délkou. Jeho obsahem je identifikátor, jehož kódování a sémantika jsou definovány operátorem. Síť může tento identifikátor číst z UE (která jej přečte z USIM) během procedur, jako je registrace nebo aktivace služby. Mechanismus funguje prostřednictvím standardizovaných příkazů mezi mobilním zařízením ([ME](/mobilnisite/slovnik/me/)) a UICC. Když síť nebo samotné ME potřebuje hodnotu GID1, vydá příkaz READ BINARY pro identifikátor souboru ([FID](/mobilnisite/slovnik/fid/)) odpovídající EF(GID1). Aplikace USIM na UICC tento příkaz zpracuje a vrátí uložená data.

V síťové architektuře GID1 používají různé síťové funkce, primárně v jádru sítě. Například profil účastníka v [HLR](/mobilnisite/slovnik/hlr/) (Home Location Register) nebo HSS (Home Subscriber Server) může být propojen s hodnotou GID1. Když se UE registruje, MSC (Mobile Switching Center) nebo SGSN (Serving GPRS Support Node) může předat GID1 do HLR/HSS. HLR/HSS pak může tento skupinový identifikátor použít jako klíč k aplikaci konkrétní servisní logiky, tarifních plánů nebo přístupových omezení definovaných pro danou skupinu. Slouží jako nástroj kategorizace účastníků v rámci operatorových Business a Operational Support Systems (BSS/OSS).

Úlohou GID1 je umožnit diferenciaci služeb na základě skupiny bez nutnosti individuálního provizionování pro každého účastníka. Je to základní prvek pro hromadné nasazování služeb, firemní plány a správu skupin pro komunikaci typu machine-to-machine (M2M). Kontrolou GID1 může síť okamžitě určit, zda účastník patří do 'premium' skupiny, skupiny pro 'machine-type communication' nebo skupiny 'partner roaming', a odpovídajícím způsobem uplatnit příslušné síťové politiky, profily kvality služeb (QoS) nebo účtovací pravidla.

## K čemu slouží

GID1 byl zaveden, aby poskytl mobilním operátorům flexibilní, na SIM kartě založený mechanismus pro správu a diferenciaci velkých skupin účastníků. Před existencí takových skupinových identifikátorů často vyžadovalo uplatňování konkrétních síťových politik nebo servisních balíčků udržování složitých, individualizovaných profilů v síťových databázích nebo používání méně bezpečných identifikátorů náchylných ke zneužití. To bylo provozně náročné pro správu firemních účtů, rodinných tarifů nebo nových kategorií služeb, jako jsou zařízení pouze pro datové služby.

Zavedení GID1 (a GID2) reagovalo na potřebu standardizovaného, bezpečného a přenosného skupinového atributu. Jeho uložení na odolnou kartu UICC/USIM zajišťuje, že skupinová příslušnost je vázána na fyzické médium předplatného, což je bezpečnější než přiřazení skupiny pouze v síti. To umožňuje, aby služby a omezení spolehlivě následovaly SIM kartu účastníka, což je zásadní pro roamingové scénáře a nezávislost na zařízení.

Historicky, jak se mobilní služby rozvíjely za hranice prostého hlasu, potřebovali operátoři jemnější nástroje pro segmentaci služeb. GID1 poskytl jednoduchý, ale účinný prvek v modulu identifikace účastníka pro spuštění skupinově specifické logiky v síti. Vyřešil problém škálovatelné správy služeb tím, že operátorům umožnil vytvářet, upravovat a nabízet služby pro celé skupiny prostým naprogramováním nebo aktualizací hodnoty GID na SIM kartách, místo rekonfigurace milionů individuálních záznamů v HLR. Toto bylo zvláště motivováno růstem služeb s přidanou hodnotou a potřebou efektivní hromadné správy účastníků.

## Klíčové vlastnosti

- Uložen v elementárním souboru EF(GID1) na USIM/UICC
- Operátorem definované kódování a sémantika pro flexibilní použití
- Čten sítí prostřednictvím standardizovaných příkazů UICC (např. READ BINARY)
- Umožňuje skupinové provizionování služeb a vynucování politik
- Poskytuje bezpečný skupinový identifikátor vázaný na SIM kartu
- Usnadňuje hromadnou správu kategorií účastníků (např. M2M, firemní uživatelé)

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [EF – Elementary File](/mobilnisite/slovnik/ef/)
- [GID2 – Group Identifier (level 2)](/mobilnisite/slovnik/gid2/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G

---

📖 **Anglický originál a plná specifikace:** [GID1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/gid1/)
