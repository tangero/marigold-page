---
slug: "ccnl"
url: "/mobilnisite/slovnik/ccnl/"
type: "slovnik"
title: "CCNL – Completion of Communications on Not Logged In"
date: 2025-01-01
abbr: "CCNL"
fullName: "Completion of Communications on Not Logged In"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ccnl/"
summary: "CCNL je služba 3GPP, která umožňuje uživateli přijímat a dokončit příchozí komunikaci (jako hovory nebo zprávy) i v případě, že je jeho zařízení odhlášeno z IMS sítě. Zajišťuje kontinuitu služby dočas"
---

CCNL je služba 3GPP, která umožňuje uživateli přijímat a dokončit příchozí komunikaci, když je jeho zařízení odhlášeno z IMS sítě, a to jeho dočasnou registrací pro danou relaci.

## Popis

Completion of Communications on Not Logged In (CCNL) je služba definovaná v rámci architektury IP Multimedia Subsystem (IMS) pro zpracování příchozích komunikačních požadavků pro uživatele, jehož zařízení není aktuálně registrováno v IMS síti. Tento stav, známý jako 'not logged in', nastává, když je User Equipment (UE) uživatele vypnuté, mimo dosah sítě, nebo se z IMS explicitně odhlásilo za účelem úspory baterie, ale síť přesto potřebuje doručit příchozí relaci, jako je například hovor Voice over LTE (VoLTE) nebo multimediální relaci. Službu CCNL vyvolá Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) při přijetí počáteční [SIP](/mobilnisite/slovnik/sip/) žádosti (např. INVITE) pro uživatele, který není registrován. S-CSCF po zjištění, že uživatel není přihlášen, zkontroluje profil služeb uživatele uložený v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Pokud je služba CCNL předplacena a aktivní, S-CSCF spustí její servisní logiku.

Klíčový mechanismus spočívá v interakci S-CSCF s Application Server ([AS](/mobilnisite/slovnik/as/)), který hostí servisní logiku CCNL. Tímto AS může být Telephony Application Server ([TAS](/mobilnisite/slovnik/tas/)) nebo dedikovaná servisní platforma. AS po přijetí podnětu od S-CSCF vyhodnotí žádost na základě konfigurace služeb uživatele a případně i preferencí účastníka (jako pravidla podle denní doby nebo filtrování volajícího). Pokud má být relace dokončena, AS instruuje S-CSCF, aby provedl 'network-initiated' nebo 'third-party' registraci jménem uživatele. Tento proces dočasně zaregistruje Public User Identity uživatele v IMS, což umožní správné směrování příchozí SIP žádosti. S-CSCF pak pokračuje ve zpracování původního požadavku na zřízení relace, jako kdyby byl uživatel registrován, a přepošle jej směrem k UE, které se musí zapnout nebo znovu připojit k síti, aby relaci přijalo.

Mezi klíčové architektonické komponenty patří S-CSCF, který funguje jako centrální uzel pro řízení relací a spouštění služeb; HSS, který ukládá profil služeb uživatele včetně údajů o předplatném CCNL; a AS, který vykonává servisní logiku. Rozhraní mezi S-CSCF a AS je typicky IMS Service Control ([ISC](/mobilnisite/slovnik/isc/)) rozhraní používající SIP. CCNL hraje klíčovou roli ve zlepšení uživatelského zážitku tím, že zabraňuje zmeškání komunikace během dočasné nepřítomnosti v síti. Je zvláště důležitá pro VoLTE a Rich Communication Services ([RCS](/mobilnisite/slovnik/rcs/)), kde se očekává bezproblémové dokončení hovoru. Služba také interaguje s dalšími IMS prvky, jako je Terminating Access Domain Selection ([T-ADS](/mobilnisite/slovnik/t-ads/)), pro výběr vhodné přístupové sítě (např. CS fallback), pokud registrace do IMS selže, což zajišťuje robustní doručení.

## K čemu slouží

CCNL byla zavedena, aby vyřešila problém zmeškané příchozí komunikace v sítích založených na IMS, jako jsou sítě poskytující VoLTE a multimediální služby. Před zavedením CCNL, pokud zařízení uživatele nebylo registrováno v IMS (např. protože bylo vypnuté, v hlubokém spánku nebo mimo dosah sítě), byly příchozí SIP požadavky na relaci sítí odmítnuty s odpovědí 'user not registered', což vedlo k zmeškanému hovoru nebo notifikaci o zprávě. To představovalo významné zhoršení oproti starším circuit-switched (CS) sítím, kde síť často mohla zařízení vyvolat a hovor dokončit, i když bylo v klidovém stavu. Motivací pro CCNL byla potřeba poskytnout stejnou úroveň služeb a kontinuitu při migraci operátorů na hlasové a messagingové služby v architekturách all-IP IMS.

Vytvoření CCNL bylo hnací silou požadavku na podporu energeticky úsporných zařízení a uživatelsky řízených stavů registrace bez obětování dostupnosti. Uživatelé se mohou z IMS explicitně odhlásit, aby ušetřili baterii, nebo zařízení mohou přejít do úsporných režimů s periodickou registrací. CCNL řeší omezení základního registračního modelu IMS tím, že umožňuje síti dočasně znovu vytvořit registrační kontext za konkrétním účelem dokončení příchozí komunikace. Tím se řeší obchodní i technický problém zajištění, aby uživatelé zůstali dostupní, což je základní očekávání pro telefonní služby. Umožňuje také nové servisní scénáře, jako je odložené zřizování relace, kdy síť může držet požadavek na relaci, dokud se uživatel nestane dostupným.

## Klíčové vlastnosti

- Umožňuje dokončení příchozí relace pro neregistrované uživatele IMS
- Spouští síťově iniciovanou registraci třetí stranou jménem uživatele
- Integruje se s profilem služeb IMS a logikou Application Server
- Podporuje konfigurovatelnou servisní logiku pro filtrování a autorizaci
- Funguje ve spolupráci s Terminating Access Domain Selection (T-ADS)
- Aplikovatelná na různé typy relací včetně hlasu, videa a zasílání zpráv

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)
- [T-ADS – Terminating Access Domain Selection](/mobilnisite/slovnik/t-ads/)

## Definující specifikace

- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 24.642** (Rel-19) — CCBS/CCNR/CCNL SIP Protocol Specification
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.292** (Rel-19) — IMS Centralized Services (ICS) Interworking

---

📖 **Anglický originál a plná specifikace:** [CCNL na 3GPP Explorer](https://3gpp-explorer.com/glossary/ccnl/)
