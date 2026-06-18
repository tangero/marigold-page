---
slug: "ceir"
url: "/mobilnisite/slovnik/ceir/"
type: "slovnik"
title: "CEIR – Central Equipment Identity Register"
date: 2025-01-01
abbr: "CEIR"
fullName: "Central Equipment Identity Register"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ceir/"
summary: "Central Equipment Identity Register (CEIR) je centralizovaná databáze, která ukládá a spravuje mezinárodní identifikátor mobilního zařízení (IMEI). Umožňuje síťovým operátorům zařazovat odcizená nebo"
---

CEIR je Central Equipment Identity Register, centralizovaná databáze, která ukládá čísla IMEI, aby umožnila síťovým operátorům zařazovat odcizená nebo podvodná zařízení na černou listinu, čímž zvyšuje bezpečnost napříč mobilními sítěmi.

## Popis

Central Equipment Identity Register (CEIR) funguje jako klíčová bezpečnostní a řídicí komponenta v architektuře sítí 3GPP, která je speciálně navržena pro boj proti krádežím mobilních zařízení a podvodům prostřednictvím centralizované správy [IMEI](/mobilnisite/slovnik/imei/). V jádru systému CEIR se nachází komplexní databáze čísel IMEI, což jsou jedinečné 15místné identifikátory přiřazené každému mobilnímu zařízení. Systém funguje tak, že přijímá data IMEI z jednotlivých registrů identit zařízení ([EIR](/mobilnisite/slovnik/eir/)) síťových operátorů a konsoliduje tyto informace do centralizovaného úložiště, k němuž mají přístup vícečetní operátoři napříč různými regiony nebo zeměmi.

Z architektonického hlediska rozhraní CEIR komunikuje s operátorskými EIR prostřednictvím standardizovaných protokolů, typicky za použití signalizační sítě [SS7](/mobilnisite/slovnik/ss7/) nebo v pozdějších verzích rozhraní založených na IP. Když se zařízení pokouší registrovat v síti, EIR obsluhující sítě dotazuje CEIR, aby ověřil stav zařízení. CEIR odpoví informací o tom, zda je zařízení na černé listině (odcizené nebo zakázané), bílé listině (schválené) nebo v šedé zóně (vyžadující další monitorování). Tento mechanismus dotaz–odpověď probíhá v reálném čase během procesů připojování zařízení, což umožňuje okamžité opatření proti neautorizovaným zařízením.

Klíčové komponenty systému CEIR zahrnují centrální databázový server, který ukládá všechny záznamy IMEI s jejich přidruženými stavovými příznaky; administrační rozhraní pro správu černých a bílých listin; stroj pro zpracování dotazů, který obsluhuje požadavky od operátorských EIR; a synchronizační mechanismy zajišťující konzistenci dat v síti. Systém také obsahuje reportovací a analytické moduly, které sledují vzorce podvodů se zařízeními a generují statistiky pro regulatorní soulad a provozní přehledy.

V provozu plní CEIR několik klíčových rolí: umožňuje blokování odcizených zařízení napříč operátory, což zabraňuje pachatelům prostě přejít po krádeži na jinou síť; podporuje regulatorní požadavky na sledování zařízení a prevenci podvodů; a poskytuje základ pro pokročilé služby, jako je ověřování záruky zařízení nebo detekce padělaných zařízení. Centralizovaná povaha CEIR umožňuje efektivní aktualizace a konzistentní vynucování pravidel napříč více operátory, čímž vytváří jednotnou frontu proti trestné činnosti spojené se zařízeními v telekomunikačním ekosystému.

## K čemu slouží

CEIR byl vytvořen, aby řešil rostoucí problém krádeží mobilních zařízení a s nimi spojené finanční ztráty pro spotřebitele, operátory a výrobce. Před jeho zavedením mohla být odcizená zařízení často používána v různých sítích, protože jednotliví operátoři udržovali oddělené databáze zařízení s omezenou koordinací. Tato fragmentace umožňovala pachatelům obejít místní černé listiny přesunem odcizených zařízení na sítě provozované jinými společnostmi nebo v jiných geografických regionech.

Historicky motivace pro CEIR vzešla z několika naléhavých potřeb: rostoucí hodnota mobilních zařízení z nich učinila atraktivní cíle pro krádeže; nedostatek koordinace mezi operátory bránil účinným protikrádežovým opatřením; a regulatorní orgány začaly požadovat lepší řešení na ochranu spotřebitelů. 3GPP uznalo, že centralizovaný přístup přinese významné výhody oproti distribuovaným systémům, včetně konzistentního vynucování pravidel, snížené administrativní zátěže pro jednotlivé operátory a zvýšené účinnosti v boji proti mezinárodnímu obchodu s odcizenými zařízeními.

CEIR tyto problémy řeší vytvořením jediného autoritativního zdroje informací o stavu zařízení, k němuž mají přístup všichni operátoři. Tím odstraňuje efekt 'bezpečného přístavu', kdy mohla být odcizená zařízení používána v sítích, které ještě neobdržely hlášení o krádeži. Systém také řeší technické výzvy, jako je synchronizace databází, výkon dotazů při vysokém zatížení a zabezpečený řízený přístup k citlivým informacím o zařízeních. Poskytnutím standardizovaného rozhraní a datového formátu CEIR umožňuje interoperabilitu mezi různými implementacemi [EIR](/mobilnisite/slovnik/eir/) od různých dodavatelů a podporuje jak národní, tak mezinárodní protikrádežové iniciativy.

## Klíčové vlastnosti

- Centralizovaná správa databáze IMEI
- Zpracování dotazů na stav zařízení v reálném čase
- Synchronizace černých listin napříč operátory
- Standardizovaná rozhraní k operátorským EIR
- Administrativní nástroje pro správu listin
- Reportovací a analytické schopnosti

## Související pojmy

- [EIR – Equipment Identity Register](/mobilnisite/slovnik/eir/)
- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [CEIR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ceir/)
