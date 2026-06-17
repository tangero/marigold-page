---
slug: "mes"
url: "/mobilnisite/slovnik/mes/"
type: "slovnik"
title: "MES – Manufacturing Execution System"
date: 2025-01-01
abbr: "MES"
fullName: "Manufacturing Execution System"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mes/"
summary: "V kontextu 3GPP označuje MES systém používaný pro automatizované, dálkové testování a konfiguraci zařízení IoT během výrobního procesu. Umožňuje hromadnou personalizaci zařízení, zřizování přihlašovac"
---

MES je systém pro automatizované, dálkové testování, konfiguraci a zřizování přihlašovacích údajů zařízení IoT během výroby, aby byla připravena k připojení do sítě ihned po vybalení.

## Popis

V rámci architektury 3GPP je Manufacturing Execution System (MES) specializovaná platforma definovaná pro průmyslovou výrobu zařízení IoT, zejména těch, která podporují technologie Cellular IoT (CIoT), jako jsou NB-IoT a LTE-M. Jeho primární funkcí je automatizace závěrečných fází výroby zařízení, které zahrnují dálkové zřizování předplatného, bezpečné vkládání přihlašovacích údajů, konfiguraci zařízení a funkční testování výkonu. MES komunikuje přímo se zařízením na výrobní lince, typicky přes lokální spojovací rozhraní (např. USB), a funguje jako důvěryhodný zprostředkovatel mezi zařízením a vzdálenými síťovými entitami, jako je Subscription Manager - Data Preparation (SM-DP+), nebo systémy operátora mobilní sítě.

Architektonicky MES pracuje v zabezpečeném výrobním prostředí. Přijímá výrobní zakázky obsahující podrobnosti, jako jsou rozsahy [IMEI](/mobilnisite/slovnik/imei/), identifikátory [ICCID](/mobilnisite/slovnik/iccid/) a profily cílového operátora. U zařízení vybavených vestavěným čipem eUICC MES usnadňuje dálkové zřizování provozních profilů. Komunikuje se serverem SM-DP+ za účelem stažení a bezpečné instalace konkrétního profilu síťového operátora na eUICC. Dále MES provádí klíčové konfigurační úkoly, jako je nastavení [APN](/mobilnisite/slovnik/apn/), konfigurace preferovaných PLMN a načítání certifikátů zařízení. Také spouští automatizované sady testů pro ověření vysokofrekvenčního výkonu, shody protokolového zásobníku a základních postupů připojení k síti, čímž zajišťuje plnou funkčnost každého zařízení před opuštěním továrny.

Role MES je klíčová pro hodnotový řetězec IoT. Mění obecný hardwarový modul v personalizovaný produkt připravený k provozu v síti. Automatizací těchto procesů odstraňuje potřebu ručního zásahu, výrazně snižuje výrobní chyby a urychluje uvedení na trh. Pro operátory mobilních sítí zaručuje, že zařízení dorazí předkonfigurovaná a otestovaná, což minimalizuje náklady na podporu a neúspěšné pokusy o aktivaci. Pro poskytovatele služeb IoT a podniky zajišťuje bezpečnost zařízení od samého počátku, protože kryptografické klíče a přihlašovací údaje jsou zřizovány v řízeném a auditovatelném prostředí. Specifikace, například v TS 22.832 a TS 37.579, definují požadavky a testovací postupy k zajištění interoperability mezi platformami MES od různých dodavatelů a zařízeními, která vyrábějí.

## K čemu slouží

Standardizace požadavků na MES v rámci 3GPP byla motivována specifickými výzvami výroby zařízení IoT. Tradiční výroba spotřebních zařízení nebyla optimalizována pro rozsah, cenová omezení a bezpečnostní potřeby IoT. Ruční konfigurace milionů senzorů nebo sledovacích zařízení pomocí přihlašovacích údajů operátora a zařízení specifických nastavení byla neúměrně drahá, pomalá a náchylná k chybám. Navíc nástup technologie eUICC, která umožňuje dálkové zřizování SIM, vyžadoval bezpečný a automatizovaný tovární proces pro prvotní vybavení zařízení jeho úvodními možnostmi zřizování.

MES byl vytvořen k řešení těchto problémů škálovatelnosti a bezpečnosti. Odstraňuje omezení nepropojených, vlastních výrobních nástrojů dodavatelů tím, že poskytuje standardizovanou referenční architekturu a požadavky na rozhraní. To výrobcům zařízení umožňuje budovat výrobní linky, které mohou bezproblémově integrovat se zázemními systémy více mobilních operátorů. Klíčový problém, který řeší, je 'poslední míle' výroby zařízení – zajištění, že každé zařízení je personalizované, ověřené a funkčně prověřené před expedicí. To je obzvláště kritické pro nasazení IoT, kde mohou být zařízení instalována na těžko dostupných místech, což činí opravy po nasazení nákladné nebo nemožné. MES zajišťuje bezúdržbovou zkušenost se zaváděním, kdy se zařízení v terénu zapne a automaticky připojí k určené síti.

## Klíčové vlastnosti

- Automatizované dálkové zřizování provozních profilů eUICC přes SM-DP+
- Bezpečné vkládání přihlašovacích údajů zařízení, certifikátů a kryptografických klíčů
- Hromadná konfigurace parametrů zařízení (např. APN, PLMN)
- Spouštění automatizovaných testovacích sad pro RF a shodu protokolů
- Integrace se systémy výrobní linky pro sledování a trasování (IMEI, ICCID)
- Generování zpráv o výkonu zařízení a zajištění kvality

## Definující specifikace

- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TR 22.832** (Rel-17) — Study on cyber-physical control in vertical domains
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 36.579** — 3GPP TR 36.579
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MES na 3GPP Explorer](https://3gpp-explorer.com/glossary/mes/)
