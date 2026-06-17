---
slug: "dam"
url: "/mobilnisite/slovnik/dam/"
type: "slovnik"
title: "DAM – DECT Authentication Module"
date: 2026-01-01
abbr: "DAM"
fullName: "DECT Authentication Module"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dam/"
summary: "Bezpečnostní modul používaný v systémech DECT (Digital Enhanced Cordless Telecommunications) pro autentizaci účastníka a správu klíčů. Bezpečně ukládá identitu účastníka a autentizační přihlašovací úd"
---

DAM je bezpečnostní modul používaný v systémech DECT, který bezpečně ukládá identitu účastníka a přihlašovací údaje pro autentizaci a správu klíčů, čímž umožňuje zabezpečený přístup k bezšňůrovým sítím.

## Popis

[DECT](/mobilnisite/slovnik/dect/) Authentication Module (DAM) je hardwarová bezpečnostní komponenta, typicky implementovaná jako čipová karta nebo vyhrazený čip, která bezpečně ukládá identitu a autentizační přihlašovací údaje účastníka v systému DECT. Obsahuje jedinečnou mezinárodní identitu přenosného uživatele (International Portable User Identity, IPUI), což je primární identifikátor účastníka pro síť DECT, a sdílený tajný autentizační klíč (K). Primární funkcí DAM je účastnit se výzva-odpověď autentizačního protokolu s pevnou částí DECT (základnovou stanicí nebo sítí). Když se přenosná část (ruční přístroj) pokouší o přístup k síti, síť odešle náhodnou výzvu (RAND). DAM použije svůj uložený tajný klíč (K) a kryptografický algoritmus (typicky DECT Standard Authentication Algorithm, DSAA) k výpočtu podepsané odpovědi (SRES). Tato SRES je odeslána zpět síti k ověření. Pokud se shoduje s vlastním výpočtem sítě, je autentizace úspěšná a relace může pokračovat. Tento proces brání neoprávněnému přístupu a klonování zařízení.

Z architektonického hlediska je DAM integrován do přenosné části DECT (Portable Part, PP), což je uživatelský ruční přístroj nebo terminál. Rozhraní má k hlavnímu procesoru PP a rádiovým komponentám. Samotný modul je navržen jako odolný proti neoprávněné manipulaci, čímž chrání tajný autentizační klíč (K) před extrakcí nebo duplikací. Autentizační proces je kritickou součástí DECT Generic Access Profile ([GAP](/mobilnisite/slovnik/gap/)), který zajišťuje interoperabilitu mezi zařízeními od různých výrobců. Kromě počáteční přístupové autentizace úspěšná autentizace také typicky spouští generování relace specifických šifrovacích klíčů používaných k šifrování hlasového a signalizačního provozu přes rozhraní vzduchu, čímž poskytuje důvěrnost.

Role DAM v celkové bezpečnostní architektuře DECT je zásadní. Působí jako kořen důvěry pro identitu účastníka. Autentizační centrum sítě udržuje databázi přiřazující IPUI k jejich odpovídajícím tajným klíčům (K). Celý systém je závislý na schopnosti DAM bezpečně provést kryptografický výpočet bez vystavení klíče. Zatímco systémy DECT mohou pracovat v 'samostatném' režimu pro rezidenční bezšňůrové telefony, koncept DAM je obzvláště klíčový pro systémy DECT s veřejným přístupem (jako služby DECT/GSM v duálním režimu nebo podnikové ústředny PBX), kde robustní správa účastníků a účtování závisí na bezpečné a nezpochybnitelné autentizaci. Návrh modulu klade důraz na přenositelnost, což umožňuje, aby uživatelský předplatný (prostřednictvím DAM) mohl být použit s různými kompatibilními ručními přístroji, podobně jako mobilita SIM karty v celulárních sítích.

## K čemu slouží

[DECT](/mobilnisite/slovnik/dect/) Authentication Module (DAM) byl vytvořen, aby poskytl standardizovanou, bezpečnou metodu pro autentizaci účastníků v sítích Digital Enhanced Cordless Telecommunications (DECT). Před digitálními bezšňůrovými standardy, jako je DECT, trpěly analogové bezšňůrové telefony závažnými bezpečnostními nedostatky, včetně snadného odposlechu a podvodného klonování identit ručních přístrojů. DAM řeší tyto problémy zavedením hardwarově zabezpečeného kryptografického autentizačního procesu. Řeší kritický problém ověření, zda je přenosná část (ruční přístroj) oprávněna používat síťové prostředky, čímž chrání síťové operátory před podvody a zajišťuje soukromí účastníků.

Historicky vývoj DECT na konci 80. a začátku 90. let 20. století směřoval k vytvoření kvalitního, interoperabilního digitálního bezšňůrového standardu pro rezidenční i podnikové použití, s veřejným síťovým přístupem jako klíčovým cílem. Pro veřejné nebo víceuživatelské podnikové systémy byl nezbytný spolehlivý model předplatného a účtování. DAM, inspirovaný úspěšným modulem SIM v GSM, poskytl tento základ. Umožňuje oddělit předplatné od fyzického ručního přístroje, což umožňuje mobilitu uživatele, snadnější výměnu zařízení a bezpečnou správu přihlašovacích údajů účastníka síťovým operátorem. To byl významný pokrok oproti proprietárním, méně bezpečným autentizačním metodám používaným v dřívějších digitálních bezšňůrových systémech.

DAM konkrétně řeší omezení spočívající v ukládání autentizačních přihlašovacích údajů v nezabezpečené, snadno čitelné paměti uvnitř ručního přístroje. Izolací tajného klíče ve vyhrazeném, proti manipulaci odolném modulu zvyšuje laťku pro útočníky pokoušející se naklonovat předplatné. Tento návrh také usnadňuje komerční model pro veřejný přístup DECT, kde operátor může vydat DAM zákazníkovi, který jej pak může použít v jakémkoli ručním přístroji kompatibilním s [GAP](/mobilnisite/slovnik/gap/). Účel této technologie přesahuje pouhou kontrolu přístupu; je to prvek umožňující odvození důvěryhodných relaních klíčů, což je nezbytné pro šifrování chránící důvěrnost hovorů na rozhraní vzduchu DECT.

## Klíčové vlastnosti

- Bezpečné uložení mezinárodní identity přenosného uživatele účastníka (International Portable User Identity, IPUI)
- Proti manipulaci odolné uložení tajného autentizačního klíče (K)
- Provádění DECT Standard Authentication Algorithm (DSAA) pro výzva-odpověď autentizaci
- Umožňuje generování šifrovacích klíčů pro šifrování přes rozhraní vzduchu
- Poskytuje přenositelnost identity účastníka mezi různými ručními přístroji DECT
- Základní komponenta pro interoperabilitu DECT Generic Access Profile (GAP)

## Související pojmy

- [DECT – Digital Enhanced Cordless Telecommunications](/mobilnisite/slovnik/dect/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.101** (Rel-20) — Service Principles for PLMNs

---

📖 **Anglický originál a plná specifikace:** [DAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/dam/)
