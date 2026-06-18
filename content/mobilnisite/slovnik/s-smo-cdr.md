---
slug: "s-smo-cdr"
url: "/mobilnisite/slovnik/s-smo-cdr/"
type: "slovnik"
title: "S-SMO-CDR – SGSN delivered Short message Mobile Originated – Charging Data Record"
date: 2025-01-01
abbr: "S-SMO-CDR"
fullName: "SGSN delivered Short message Mobile Originated – Charging Data Record"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/s-smo-cdr/"
summary: "Záznam o účtování dat (Charging Data Record) generovaný SGSN pro mobilním zařízením odeslanou krátkou zprávu (SMS) přenášenou přes okruhově komutovanou (CS) doménu v síti GSM/UMTS 2G/3G. Obsahuje podr"
---

S-SMO-CDR je záznam o účtování dat (Charging Data Record) generovaný SGSN pro mobilním zařízením odeslanou SMS přenášenou přes okruhově komutovanou doménu, obsahující podrobnosti o události pro offline účtování v sítích 2G/3G.

## Popis

[SGSN](/mobilnisite/slovnik/sgsn/) delivered Short message Mobile Originated – Charging Data Record (S-SMO-CDR) je specifický typ záznamu o účtování dat ([CDR](/mobilnisite/slovnik/cdr/)) definovaný v 3GPP specifikacích pro účtování. Je generován Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) v síti GSM/UMTS při zpracování mobilním zařízením odeslané služby krátkých zpráv ([SMS](/mobilnisite/slovnik/sms/)), která je doručována přes okruhově komutovanou ([CS](/mobilnisite/slovnik/cs/)) doménu jádra sítě. Tento CDR je součástí offline účtovacího systému, kde jsou informace o účtování shromažďovány po uskutečnění služební události pro pozdější zpracování a fakturaci. S-SMO-CDR obsahuje standardizovanou sadu polí, která detailně popisují SMS transakci a poskytují fakturačnímu systému potřebná data k účtování služby účastníkovi.

Generování S-SMO-CDR je spuštěno konkrétní událostí: úspěšným odesláním mobilním zařízením odeslané SMS z UE do centra služby krátkých zpráv ([SMSC](/mobilnisite/slovnik/smsc/)) přes CS doménu, kde je SGSN zapojen do směrování. Procedura typicky zahrnuje odeslání SMS z UE přes signalizační kanály CS domény (např. přes [SDCCH](/mobilnisite/slovnik/sdcch/) v GSM). [MSC](/mobilnisite/slovnik/msc/), které zpracovává CS doménu, interaguje se SGSN (pokud je účastník také přihlášen k GPRS) pro koordinaci. Po úspěšném doručení odeslané SMS dalšímu síťovému prvku (směrem k MSC) shromáždí Charging Trigger Function (CTF) SGSN příslušná data do S-SMO-CDR. Tento záznam je poté přeposlán přes rozhraní Ga do funkce Charging Gateway Function (CGF) pomocí protokolů jako GTP' nebo FTAM.

Obsah S-SMO-CDR je detailně definován v 3GPP TS 32.251 a souvisejících specifikacích. Mezi klíčová pole patří IMSI odesílajícího účastníka, MSISDN (pokud je dostupné), adresa SGSN, adresa MSC, které SMS zpracovalo, adresa centra služeb (SMSC), časová razítka pro přijetí odeslání SMS a jeho přeposlání, příčina ukončení a objem dat spojený se SMS (což je v podstatě délka zprávy). Může také zahrnovat informace o poloze (Cell Global Identity nebo Routing Area) a identifikátory pro konkrétní účtovací relaci. Tato strukturovaná data umožňují fakturačnímu systému aplikovat správný tarif pro SMS událost, který může záviset na faktorech jako cílová destinace, denní doba nebo tarifní plán účastníka.

Je důležité odlišit S-SMO-CDR od jiných SMS souvisejících CDR. Například S-SMT-CDR je generován pro mobilním zařízením přijatou SMS. Dále, pokud je SMS doručována přes paketově komutovanou (PS) doménu (jako SMS přes GPRS nebo SMS přes IP), používají se jiné typy CDR, například S-SMO-CDR pro PS doménu. S-SMO-CDR (CS doména) je starší typ CDR primárně relevantní pro sítě 2G a 3G, kde byla SMS dominantní službou a často přenášena přes signalizační rovinu CS domény. Jeho generování je základní funkcí účtovacího subsystému SGSN a přispívá k přesné monetizaci nedatových služeb v tradičních mobilních sítích.

## K čemu slouží

S-SMO-CDR byl standardizován, aby vyřešil potřebu přesného a detailního účtování událostí služby krátkých zpráv (SMS) v sítích GSM a UMTS, konkrétně pro zprávy odeslané z mobilního zařízení a směrované přes okruhově komutované jádro sítě. Před detailní standardizací potřebovali operátoři konzistentní způsob zachycení fakturačních informací pro SMS, která se rychle stala významnou službou generující příjmy. Problém byl, že doručení SMS zahrnuje více síťových uzlů (UE, BSS, MSC, SGSN, SMSC) a účtovací data musela být shromážděna v příslušném bodě kontroly – SGSN, které spravuje mobilitu účastníka a kontext relace v paketově komutované doméně, dokonce i pro tuto službu v CS doméně.

Vytvoření S-SMO-CDR bylo motivováno rozdělenou architekturou sítí 2G/3G, kde SGSN (uzel PS domény) mohlo být zapojeno do aktivit účastníka, i když samotná služba (jako hovor nebo SMS) používala CS doménu. To se děje, protože účastník může být současně přihlášen k CS i PS doménám. SGSN, které má přehled o PS přihlášení a poloze účastníka, je logickým bodem pro generování CDR pro určité CS služby jako SMS, aby zajistilo, že účtovací data jsou korelovatelná s celkovou relací účastníka. Vyřešilo to problém přiřazení SMS události správnému účastníkovi a shromažďování konzistentních dat (jako poloha, časová razítka a obsluhující uzly) napříč všemi operátory pro interoperabilitu účtovacích systémů.

Dále umožnilo flexibilní fakturační modely. Poskytnutím standardizovaného záznamu s poli pro čas, cíl (implicitně v adrese SMSC) a polohu mohli operátoři implementovat komplexní tarifní plány, jako je účtování různých sazeb za mezinárodní SMS, slevy mimo špičku nebo balíčky SMS. S-SMO-CDR, jako součást širšího rámce offline účtování 3GPP, umožnil operátorům spolehlivě sbírat data o využití ze síťových prvků, přenášet je do centrálního fakturačního systému a generovat položkové účty pro účastníky. Jeho definice byla kritickým krokem v komercializaci mobilního zasílání zpráv a zajištění, že síťová infrastruktura může podporovat její fakturaci transparentně a přesně.

## Klíčové vlastnosti

- Generován SGSN pro mobilním zařízením odeslanou SMS doručovanou přes okruhově komutovanou (CS) doménu jádra sítě.
- Součást offline účtovacího systému 3GPP, používaný pro fakturaci po události.
- Obsahuje klíčová pole jako IMSI, MSISDN, adresy SGSN/MSC, adresu SMSC, časová razítka a informace o poloze.
- Spuštěn při úspěšném odeslání SMS z UE směrem do sítě.
- Přenesen ze SGSN do Charging Gateway Function (CGF) přes rozhraní Ga pomocí protokolu GTP'.
- Odlišný od SMS CDR pro PS doménu a od CDR pro mobilním zařízením přijaté SMS (S-SMT-CDR).

## Související pojmy

- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)
- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [S-SMT-CDR – SGSN delivered Short message Mobile Terminated – Charging Data Record](/mobilnisite/slovnik/s-smt-cdr/)

## Definující specifikace

- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.295** (Rel-19) — 3GPP Charging: CDR Transfer via GTP' Protocol

---

📖 **Anglický originál a plná specifikace:** [S-SMO-CDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-smo-cdr/)
