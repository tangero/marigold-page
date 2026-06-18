---
slug: "vcs"
url: "/mobilnisite/slovnik/vcs/"
type: "slovnik"
title: "VCS – Virtual Circuit Service"
date: 2025-01-01
abbr: "VCS"
fullName: "Virtual Circuit Service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vcs/"
summary: "Služba přenosu (bearer service) v sítích 3GPP, která poskytuje spojově orientovanou přenosovou cestu podobnou okruhovému přepojování se zaručenou šířkou pásma a kvalitou. Je klíčová pro starší datové"
---

VCS je služba přenosu (bearer service) podle 3GPP, která poskytuje spojově orientovanou přenosovou cestu podobnou okruhovému přepojování se zaručenou šířkou pásma a kvalitou pro starší aplikace vyžadující předvídatelný výkon.

## Popis

Služba virtuálního okruhu (Virtual Circuit Service, VCS) je standardizovaná služba přenosu definovaná v architektuře 3GPP, určená speciálně pro okruhově přepínaná data ([CSD](/mobilnisite/slovnik/csd/)) a později vylepšené datové služby. Funguje tak, že před zahájením přenosu dat vytvoří virtuální, spojově orientovanou cestu mezi dvěma koncovými body, čímž napodobuje charakteristiky tradičního pronajatého okruhu nebo okruhově přepínaného spojení přes paketově orientovanou síťovou infrastrukturu. Tato cesta garantuje specifické parametry kvality služby (QoS), včetně šířky pásma, zpoždění a chybovosti, které jsou vyjednány během fáze navázání spojení. Službu spravují entity jádra sítě, přičemž funkce řízení hovoru a správy mobility zajišťují udržování virtuálního okruhu při pohybu uživatelského zařízení, čímž poskytují stabilní a předvídatelný komunikační kanál.

Z architektonického hlediska se VCS opírá o okruhově přepínanou ([CS](/mobilnisite/slovnik/cs/)) doménu jádra sítě a komunikuje s entitami jako je ústředna mobilní sítě ([MSC](/mobilnisite/slovnik/msc/)) a přechodová MSC ([GMSC](/mobilnisite/slovnik/gmsc/)). Služba využívá specifické protokoly pro adaptaci a přenos dat přes rozhraní rádiového přístupu a jádro sítě. Například používá mezisíťové funkce ([IWF](/mobilnisite/slovnik/iwf/)) pro přizpůsobení formátů uživatelských dat (např. z faxového přístroje nebo modemu) do formátu vhodného pro přenos přes rádiovou přístupovou síť UMTS nebo GSM. Přes rádiové rozhraní se často používá protokol [RLP](/mobilnisite/slovnik/rlp/) (Radio Link Protocol) k zajištění spolehlivého spoje, který opravuje chyby a řídí tok dat, aby byly dodrženy záruky QoS virtuálního okruhu.

Mezi klíčové komponenty zapojené do VCS patří funkce adaptace terminálu ([TAF](/mobilnisite/slovnik/taf/)) v uživatelském zařízení, která přizpůsobuje koncové zařízení pro mobilní ukončení, a mezisíťová funkce (IWF) v síti, která zajišťuje připojení k externím sítím, jako je [PSTN](/mobilnisite/slovnik/pstn/) nebo ISDN. Služba je definována v řadě technických specifikací pokrývajících popis služby, účtování a správu. Její role byla významná pro umožnění raných mobilních datových aplikací, jako je přenos faxů, vytáčené připojení k síti a služby zabezpečených transakcí, které vyžadovaly konzistentní výkon, jaký původně nemohly garantovat paketově přepínané služby typu 'best-effort'.

## K čemu slouží

Služba virtuálního okruhu byla vytvořena za účelem poskytování spolehlivých, spojově orientovaných datových služeb přes mobilní sítě 2G a 3G, které by řešily potřebu předvídatelného výkonu podobného pevným pronajatým okruhům. Před rozšířením paketově přepínaných dat (GPRS, UMTS PS) mobilní datové aplikace jako fax, terminály pro elektronické platby a vzdálený přístup vyžadovaly pro správnou funkci garantovanou šířku pásma a nízkou latenci. VCS toto vyřešila napodobením chování okruhového přepojování přes mobilní síť, čímž zajistila vyhrazené prostředky po dobu trvání hovoru.

Motivace pramenila z omezení raných mobilních sítí, které byly primárně navrženy pro hlas. Pro podporu dat potřebovala síť metodu pro statické přidělování prostředků rádiového přístupu a jádra sítě, která by poskytovala jasnou smlouvu o úrovni služeb. VCS tuto mezeru zaplnila a umožnila podnikovým aplikacím a komunikaci mezi stroji (M2M) přejít na bezdrátové připojení. Poskytla migrační cestu pro starší zařízení závislá na spojích s konstantní přenosovou rychlostí.

Historicky byl VCS základním datovým přenosem v GSM a raných vydáních UMTS. Představoval klíčový krok ve vývoji mobilních sítí, který dokázal proveditelnost datových služeb před masovým přijetím IP-based paketového přepojování. Ačkoli byl z velké části nahrazen efektivnějšími paketově přepínanými přenosy s pokročilým QoS (jako jsou dedikované přenosy v LTE/5G), jeho principy garantované služby ovlivnily pozdější rámce QoS ve standardech 3GPP.

## Klíčové vlastnosti

- Spojově orientovaný přenos dat s definovanými procedurami pro navázání a ukončení spojení
- Garantovaná šířka pásma a parametry kvality služby (QoS) po dobu trvání relace
- Podpora transparentního a netransparentního datového režimu pro zpracování chyb
- Propojení s externími okruhově přepínanými sítěmi, jako je PSTN/ISDN
- Podpora mobility s udržováním virtuálního okruhu během předávání hovoru
- Definované modely účtování založené na době spojení a objemu přenesených dat

## Definující specifikace

- **TS 23.044** (Rel-4) — GSM Teletex Service Support
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.276** (Rel-19) — VCS Online Charging from Proxy Function
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 32.296** (Rel-19) — Online Charging System (OCS) Architecture
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP

---

📖 **Anglický originál a plná specifikace:** [VCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/vcs/)
