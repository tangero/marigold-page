---
slug: "mops"
url: "/mobilnisite/slovnik/mops/"
type: "slovnik"
title: "MOPS – Million Operations Per Second"
date: 2025-01-01
abbr: "MOPS"
fullName: "Million Operations Per Second"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mops/"
summary: "Výkonnostní metrika používaná k měření výpočetního výkonu nebo propustnosti systému, zejména v kontextu operací SIM karet nebo kryptografických funkcí. Udává, kolik operací může komponenta provést za"
---

MOPS je výkonnostní metrika udávající, kolik operací může komponenta, například SIM karta nebo kryptografické funkce, provést za jednu sekundu, a slouží k měření výpočetního výkonu.

## Popis

Million Operations Per Second (MOPS) je jednotka měření představující rychlost jednoho milionu dokončených operací za sekundu. V rámci specifikací 3GPP se tato metrika primárně používá k benchmarkování a specifikaci požadavků na výkon modulu SIM (Subscriber Identity Module), zejména v kontextu univerzální integrované obvodové karty (UICC) a vestavěné SIM (eSIM). „Operacemi“ se obvykle rozumí kryptografické nebo výpočetní úlohy nezbytné pro zabezpečení sítě a autentizaci účastníka, jako je provádění autentizačních algoritmů (např. Milenage pro 3G/4G/5G), generování kryptografických klíčů nebo provádění digitálních podpisů.

Měření je klíčové pro definici minimálních výkonnostních charakteristik hardwaru UICC, aby bylo zajištěno, že může podporovat požadované bezpečnostní procedury v přijatelných časových limitech, zejména s tím, jak se algoritmy stávají složitějšími a autentizační procesy častějšími (např. u IoT zařízení s malými datovými přenosy). Specifikace jako TS 26.952 (pro výkon USIM) podrobně popisují testovací postupy a minimální hodnoty MOPS pro různé třídy aplikací UICC/USIM. Například USIM určená pro špičkový smartphone může mít vyšší požadavek na MOPS než ta určená pro IoT senzor s nízkou spotřebou, což odráží rozdíly v očekávaných vzorcích použití a autentizační zátěži.

Kromě SIM karet může MOPS sloužit jako obecný výkonnostní ukazatel pro další síťové komponenty zapojené do intenzivního zpracování, jako jsou bezpečnostní brány nebo síťové funkce provádějící šifrování/dešifrování ve velkém měřítku. Poskytuje standardizovaný způsob porovnání výpočetní propustnosti různých hardwarových implementací. Ve vývoji mobilních sítí rostoucí schopnosti MOPS umožňují robustnější zabezpečení (prostřednictvím silnějších, výpočetně náročnějších algoritmů), rychlejší časy navázání spojení a schopnost zvládnout obrovské množství současných autentizačních požadavků od IoT zařízení, což je klíčový požadavek pro scénáře 5G massive Machine-Type Communication (mMTC).

## K čemu slouží

Specifikace požadavků na MOPS vznikla z potřeby garantovat konzistentní uživatelský zážitek a výkon síťového zabezpečení napříč SIM kartami od různých výrobců. Rané SIM karty měly různou rychlost zpracování, což mohlo vést k patrným zpožděním při registraci do sítě nebo navázání hovoru, nebo dokonce způsobit selhání časově citlivých autentizačních procedur. Definování minimálního prahu MOPS zajistilo, že všechny kompatibilní SIM karty splní základní úroveň výkonu, a zabránilo tak tomu, aby podstandardní komponenty degradovaly celkový výkon sítě.

S vývojem mobilních služeb rostly i výpočetní nároky na SIM/UICC. Zavedení 3G a algoritmu Milenage, následované autentizací 4G a 5G, vyžadovalo vyšší výpočetní výkon. Dále nové případy užití, jako je IoT, vyžadovaly SIM karty, které byly nejen levné a s nízkou spotřebou, ale také schopné efektivně zvládnout autentizaci obrovského množství zařízení. Metrika MOPS umožňuje kategorizaci výkonnostních tříd UICC přizpůsobených různým typům zařízení – od základních IoT modulů po vysoce výkonná automobilová nebo mobilní broadbandová zařízení. Řeší problém zajištění toho, aby zabezpečení, jakožto základní aspekt mobilních sítí, nebylo úzkým hrdlem pro dostupnost služeb nebo bodem selhání při vysoké zátěži.

## Klíčové vlastnosti

- Standardizovaná metrika pro měření výpočetního výkonu UICC/USIM
- Benchmarkuje propustnost kryptografických operací (např. autentizací za sekundu)
- Umožňuje klasifikaci SIM karet pro různé kategorie zařízení
- Zajišťuje konzistentní časy autentizace a uživatelský zážitek
- Podporuje škálovatelnost pro masivní nasazení IoT
- Poskytuje základ pro testování shody a certifikaci

## Definující specifikace

- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.976** (Rel-19) — AMR-WB Codec Characterization & Verification
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [MOPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mops/)
