---
slug: "prl"
url: "/mobilnisite/slovnik/prl/"
type: "slovnik"
title: "PRL – Preferred Roaming List"
date: 2025-01-01
abbr: "PRL"
fullName: "Preferred Roaming List"
category: "Mobility"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/prl/"
summary: "Seznam uložený v mobilním zařízení (např. na USIM nebo v paměti zařízení), který definuje preferované sítě a frekvence pro roaming. Usměrňuje proces výběru sítě zařízením, přičemž upřednostňuje určité"
---

PRL je seznam uložený v mobilním zařízení, který definuje preferované sítě a frekvence pro roaming, aby usměrňoval výběr sítě a upřednostňoval určité operátory.

## Popis

Preferred Roaming List (PRL) je databáze nebo konfigurační soubor používaný v mobilních zařízeních, zejména v sítích [CDMA](/mobilnisite/slovnik/cdma/) a později vícemódových (např. CDMA/LTE), pro správu výběru sítě během roamingu. Obsahuje informace o preferovaných poskytovatelích služeb, technologiích rádiového přístupu ([RAT](/mobilnisite/slovnik/rat/)) a kmitočtových pásmech, která by zařízení mělo používat, když se nachází mimo pokrytí domácí sítě. PRL je typicky zajišťován operátorem domácí sítě a je uložen na [USIM](/mobilnisite/slovnik/usim/) (Universal Subscriber Identity Module) zařízení nebo v nevolatilní paměti, což umožňuje zařízení činit při vyhledávání dostupných sítí inteligentní rozhodnutí.

Z architektonického hlediska se PRL skládá ze záznamů, které mapují geografické regiony (pomocí systémových identifikátorů, [SID](/mobilnisite/slovnik/sid/), a síťových identifikátorů, [NID](/mobilnisite/slovnik/nid/)) na preferované sítě spolu s přidruženými prioritami a parametry pro akvizici. Když zařízení ztratí spojení se svou domácí sítí, nahlédne do PRL, aby určilo, na které sítě se pokusí zaregistrovat a v jakém pořadí. Seznam může zahrnovat jak partnerské sítě domácího operátora (pro plynulý roaming), tak i partnery, přičemž explicitně vylučuje zakázané nebo nežádoucí sítě. Mezi klíčové komponenty patří tabulková struktura PRL, která definuje roamingové preference podle RAT (např. CDMA, LTE, NR), a mechanismy aktualizace, které umožňují operátorům vzdáleně obnovovat seznam prostřednictvím over-the-air ([OTA](/mobilnisite/slovnik/ota/)) provize, aby se přizpůsobily měnícím se roamingovým dohodám.

Jak to funguje: Po zapnutí nebo při ztrátě pokrytí zařízení vyhledá dostupné sítě a porovná je se záznamy v PRL. Podle hodnocení v PRL upřednostňuje sítě a pokouší se připojit k nejvyšší prioritní dostupné síti. Například u vícemódového zařízení může PRL v určitých regionech upřednostnit sítě LTE před CDMA, aby využilo lepší datové služby. PRL také zahrnuje parametry akvizice, jako jsou frekvenční kanály nebo třídy pásem, což urychluje proces vyhledávání. Tento systém zajišťuje, že uživatelé při roamingu zažívají minimální narušení služeb, a operátoři mohou směrovat provoz ke nákladově efektivním nebo kvalitním partnerským sítím, čímž řídí roamingové výdaje a kvalitu služeb.

## K čemu slouží

PRL bylo představeno ve 3GPP Release 7, navazujíc na dřívější standardy [CDMA](/mobilnisite/slovnik/cdma/), aby řešilo výzvy výběru sítě v roamingových scénářích, zejména když mobilní zařízení začala podporovat více [RAT](/mobilnisite/slovnik/rat/) a rostla globální mobilita. Před zavedením PRL mohla zařízení náhodně vybírat dostupné sítě nebo se spoléhat na základní prioritní seznamy, což vedlo k neoptimálním spojením, vyšším roamingovým nákladům nebo odmítnutí služby. Motivací bylo dát operátorům kontrolu nad roamingovou zkušeností a zajistit, aby se zařízení připojovala k preferovaným partnerům nabízejícím výhodné sazby, spolehlivé služby nebo splňujícím regulatorní požadavky.

Vytvoření PRL vyřešilo problémy jako 'rogue roaming', kdy se zařízení mohla připojit k neautorizovaným sítím způsobujícím bezpečnostní rizika nebo problémy s fakturací. Poskytnutím kurátorského seznamu mohli operátoři směrovat provoz k důvěryhodným partnerům, optimalizovat síťové zdroje a zvýšit spokojenost uživatelů prostřednictvím plynulých předávání. V regionech se složitým regulatorním prostředím PRL pomáhá prosazovat národní roamingové politiky nebo se vyhýbat omezeným sítím.

Historicky se PRL vyvinulo z potřeby efektivního řízení roamingu v sítích CDMA, protože tyto sítě postrádaly globální standardy založené na SIM jako GSM. S konvergencí k LTE a 5G se role PRL rozšířila o více-RAT prioritizaci, podporující plynulé přechody mezi technologiemi. Zůstává relevantní pro správu interoperability se staršími systémy a optimalizaci konektivity v heterogenních sítích, ačkoli v čistých nasazeních 5G SA může výběr sítě více záviset na prioritách založených na USIM (např. seznamy výběru PLMN). PRL je příkladem toho, jak lze operační kontrolu vložit do zařízení, aby byla vyvážena uživatelská mobilita s obchodními a technickými cíli operátora.

## Klíčové vlastnosti

- Ukládá prioritní seznam sítí a RAT pro roamingový výběr
- Konfigurovatelný pomocí OTA aktualizací od domácího operátora
- Zahrnuje geografické mapování (SID/NID) a frekvenční parametry
- Podporuje vícemódová zařízení (např. CDMA, LTE, NR)
- Umožňuje směrování ke nákladově efektivním nebo kvalitním partnerským sítím
- Snižuje čas skenování sítě tím, že poskytuje akviziční data

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TR 22.936** (Rel-19) — Multi-system terminal behavior study

---

📖 **Anglický originál a plná specifikace:** [PRL na 3GPP Explorer](https://3gpp-explorer.com/glossary/prl/)
