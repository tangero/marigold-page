---
slug: "cpdu"
url: "/mobilnisite/slovnik/cpdu/"
type: "slovnik"
title: "CPDU – Command Protocol Data Unit"
date: 2025-01-01
abbr: "CPDU"
fullName: "Command Protocol Data Unit"
category: "Protocol"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/cpdu/"
summary: "Standardizovaná protokolová datová jednotka používaná pro řízení testovacích zařízení a měřicí příkazy při 3GPP konformním testování. Umožňuje automatizované testování RF výkonu UE tím, že poskytuje s"
---

CPDU je standardizovaná protokolová datová jednotka používaná pro řízení testovacích zařízení a měřicí příkazy při 3GPP konformním testování uživatelských zařízení.

## Popis

Command Protocol Data Unit (CPDU) je základní protokolový prvek definovaný v 3GPP TS 34.131 pro řízení testovacích zařízení během testování rádiové frekvence (RF) uživatelského zařízení (UE) na konformitu. Slouží jako standardizovaný formát zpráv pro přenos testovacích příkazů, měřicích požadavků a odpovídajících odpovědí mezi řadičem testovacího systému a testovacím zařízením nebo testovaným UE. Struktura CPDU zahrnuje povinná hlavičková pole obsahující verzi protokolu, typ zprávy, sekvenční čísla a délku zprávy, následovaná sekcemi s proměnnou délkou, které nesou konkrétní testovací parametry, konfigurace měření nebo výsledná data.

Zprávy CPDU fungují v rámci architektury klient-server, kde testovací systém vystupuje jako klient vydávající příkazy a testovací zařízení nebo UE funguje jako server, který tyto příkazy provádí a vrací odpovědi. Protokol podporuje synchronní a asynchronní režimy komunikace s komplexními mechanismy pro zpracování chyb včetně správy časových limitů, postupů opakování a hlášení stavu. Každá CPDU obsahuje jedinečný identifikátor transakce, který umožňuje korelaci mezi příkazy a jejich odpovídajícími odpověďmi, což zajišťuje spolehlivé provádění testů i ve složitých vícekrokových testovacích scénářích.

Protokol definuje více typů zpráv včetně příkazových zpráv pro zahájení testovacích postupů, odpovědních zpráv pro potvrzení provedení příkazu, zpráv s měřicími požadavky pro konfiguraci RF měření a zpráv s výsledky měření pro hlášení výsledků testů. Datové části (payload) CPDU jsou kódovány pomocí standardizovaných datových formátů, které zajišťují interoperabilitu mezi různými výrobci testovacích zařízení a implementacemi UE. Protokol zahrnuje mechanismy pro správu relací, přidělování prostředků a synchronizaci testovacího stavu, což umožňuje provádět složité testovací sekvence s přesnými požadavky na časování a koordinaci.

V praktické implementaci jsou zprávy CPDU obvykle přenášeny přes sítě TCP/IP mezi komponentami testovacího systému, ačkoli specifikace 3GPP připouští i jiné transportní mechanismy. Protokol zahrnuje mechanismy řízení toku, aby se zabránilo přetížení testovacího systému, a podporuje transakce s jedním příkazem i dávkové sekvence příkazů pro vyšší efektivitu. Bezpečnostní prvky v implementacích CPDU zajišťují, že pouze autorizované testovací systémy mohou ovládat citlivá RF testovací zařízení, přičemž jsou specifikovány mechanismy autentizace a autorizace pro produkční testovací prostředí.

## K čemu slouží

Protokol CPDU byl vytvořen, aby řešil rostoucí složitost a problémy s interoperabilitou mezi různými výrobci při 3GPP konformním testování UE. Před jeho standardizací používali výrobci testovacích zařízení proprietární příkazové protokoly, které vyžadovaly vlastní integraci pro každé testovací uspořádání, což vedlo ke zvýšeným nákladům na vývoj, delším časům nasazení testovacích systémů a nekonzistentním výsledkům testů v různých laboratořích. Proprietární přístupy také ztěžovaly síťovým operátorům a regulačním orgánům porovnávat výsledky testů od různých výrobců zařízení, což komplikovalo certifikační procesy.

Zavedením standardizovaného příkazového protokolu ve vydání 8 (Release 8) umožnil 3GPP skutečnou plug-and-play interoperabilitu mezi testovacími systémy od různých výrobců, což významně snížilo čas a náklady spojené s integrací testovacích systémů. Protokol CPDU poskytuje společný jazyk pro všechna RF konformní testování a zajišťuje, že testovací příkazy jsou konzistentně interpretovány v různých implementacích testovacích zařízení. Tato standardizace byla obzvláště důležitá, protože technologie 3GPP se vyvíjely a zahrnovaly složitější RF požadavky, jako je agregace nosných, konfigurace [MIMO](/mobilnisite/slovnik/mimo/) a pokročilé mechanismy řízení výkonu, které vyžadovaly sofistikovanou testovací automatizaci.

Protokol také řeší potřebu automatizovaného, opakovatelného testování ve velkém měřítku, která se stala nezbytnou s dramatickým nárůstem objemů výroby mobilních zařízení. Poskytnutím standardizovaného rozhraní pro automatizaci testů umožňuje CPDU prostředím pro testování ve velkosériové výrobě dosáhnout konzistentní kontroly kvality při současném snížení manuálního zásahu. Návrh protokolu akomoduje budoucí testovací požadavky prostřednictvím rozšiřitelných formátů zpráv a mechanismů správy verzí, což zajišťuje zpětnou kompatibilitu a zároveň umožňuje zavádění nových testovacích schopností s vývojem specifikací 3GPP.

## Klíčové vlastnosti

- Standardizovaný formát zpráv pro řízení testovacích zařízení
- Interoperabilita nezávislá na výrobci pro konformní testování
- Podpora synchronních a asynchronních režimů komunikace
- Komplexní mechanismy pro zpracování chyb a opakování
- Rozšiřitelná struktura datové části pro budoucí testovací požadavky
- Správa transakcí s jedinečnými identifikátory pro korelaci příkaz-odpověď

## Definující specifikace

- **TS 34.131** (Rel-19) — SIM API C Language Test Specification

---

📖 **Anglický originál a plná specifikace:** [CPDU na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpdu/)
