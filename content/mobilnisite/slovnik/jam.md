---
slug: "jam"
url: "/mobilnisite/slovnik/jam/"
type: "slovnik"
title: "JAM – Java Application Manager"
date: 2025-01-01
abbr: "JAM"
fullName: "Java Application Manager"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/jam/"
summary: "Komponenta v mobilním zařízení, která spravuje životní cyklus aplikací v Javě (MIDlety). Zavedená ve specifikaci 3GPP Release 5, zajišťuje instalaci, spouštění, aktualizaci a odstranění aplikací v Jav"
---

JAM je komponenta mobilního zařízení zavedená ve specifikaci 3GPP Release 5, která spravuje životní cyklus aplikací v Javě (MIDlety) tím, že na základě deskriptorů zajišťuje jejich instalaci, spouštění, aktualizaci a odstranění.

## Popis

Java Application Manager (JAM) je runtime manažerská entita v mobilním zařízení odpovědná za aplikace v Javě, které jsou v souladu s Mobile Information Device Profile ([MIDP](/mobilnisite/slovnik/midp/)). Jedná se o softwarový modul, který je typicky součástí Java runtime prostředí zařízení. JAM komunikuje se soubory Java Application Descriptor ([JAD](/mobilnisite/slovnik/jad/)), aby řídil životní cyklus aplikace. Mezi jeho hlavní funkce patří: parsování JAD souborů pro získání metadat a požadavků aplikace; ověření, že prostředí zařízení (paměť, Java [API](/mobilnisite/slovnik/api/), oprávnění) splňuje potřeby aplikace; stažení a instalace přidruženého Java Archive (JAR); spuštění a správa provádění MIDletů; zpracování aktualizací a odstranění; a vynucování bezpečnostních politik během běhu.

Z architektonického hlediska se JAM nachází mezi operačním systémem zařízení, síťovým provisioning systémem a Java virtual machine. Jako důvěryhodný zdroj informací pro rozhodování o správě používá JAD. Mezi klíčové komponenty jeho činnosti patří parser deskriptorů, kontrola kompatibility, bezpečnostní manažer, který komunikuje s bezpečnostními frameworky zařízení, instalační engine a kontrolér životního cyklu pro stavy MIDletů (např. pozastavený, zničený). Jeho role v síťovém ekosystému spočívá v tom, že je lokálním koncovým bodem pro služby správy aplikací, což uživatelům umožňuje bezpečnou a spolehlivou interakci s aplikacemi poskytovanými na dálku.

JAM zajišťuje, že aplikace běží v řízeném sandboxu a respektují oprávnění deklarovaná v JAD. Spravuje přidělování zdrojů pro MIDlety a může ukončit aplikace, které porušují politiky nebo vyčerpají zdroje. Specifikace podrobně popisuje, jak JAM reaguje na provisioning příkazy, zpracovává chybové stavy a komunikuje s uživatelským rozhraním pro výběr aplikací. Jedná se o klíčový prvek pro model řízené distribuce aplikací, který poskytuje lokální důvěryhodný bod pro provádění.

## K čemu slouží

JAM byl vytvořen, aby poskytl standardizovanou a bezpečnou správcovskou vrstvu pro aplikace v Javě na mobilních zařízeních. Bez vyhrazeného manažera by instalace a provádění aplikací byly nekontrolované, což by představovalo riziko pro stabilitu zařízení, bezpečnost a uživatelský zážitek. Růst stahovatelných mobilních služeb vyžadoval důvěryhodnou entitu v zařízení, která by zprostředkovávala komunikaci mezi externími provisioning systémy a lokálním Java runtime prostředím.

Jeho účelem je řešit problémy správy životního cyklu aplikací v omezeném mobilním prostředí. Zajišťuje, že jsou instalovány a spouštěny pouze kompatibilní a autorizované aplikace. Spravuje omezené zdroje zařízení (paměť, výpočetní výkon) mezi více aplikacemi. Vynucováním bezpečnostních politik na základě informací z deskriptorů chrání zařízení a uživatelská data před škodlivými nebo nekorektně se chovajícími aplikacemi. Zavedený spolu s [JAD](/mobilnisite/slovnik/jad/) v Release 5, JAM dokončil framework pro nasaditelný a spravovatelný ekosystém aplikací v Javě, který byl klíčový pro rané poskytování mobilního obsahu a služeb.

## Klíčové vlastnosti

- Správa životního cyklu pro Java MIDlety (instalace, běh, aktualizace, odstranění)
- Parsuje a validuje soubory Java Application Descriptor (JAD)
- Před instalací provádí kontrolu kompatibility zařízení a bezpečnostní kontrolu
- Vynucuje runtime bezpečnostní oprávnění a limity zdrojů
- Komunikuje se síťovými provisioning systémy pro OTA aktualizace
- Poskytuje uživatelské rozhraní pro výběr a ovládání aplikací

## Související pojmy

- [JAD – Java Application Descriptor](/mobilnisite/slovnik/jad/)

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [JAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/jam/)
