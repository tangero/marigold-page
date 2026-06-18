---
slug: "ssh"
url: "/mobilnisite/slovnik/ssh/"
type: "slovnik"
title: "SSH – Secure Shell"
date: 2026-01-01
abbr: "SSH"
fullName: "Secure Shell"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ssh/"
summary: "Kryptografický síťový protokol pro zabezpečené vzdálené přihlašování a provádění příkazů přes nezabezpečenou síť. Poskytuje silné ověřování a šifrovanou komunikaci dat, čímž nahrazuje nezabezpečené pr"
---

SSH je kryptografický síťový protokol používaný v systémech 3GPP pro zabezpečené vzdálené přihlašování, provádění příkazů a šifrovanou správu síťových prvků přes nezabezpečené sítě.

## Popis

Secure Shell (SSH) je soubor protokolů, standardizovaný v rámci 3GPP pro zabezpečený přístup k síťovým službám, který funguje na aplikační vrstvě. Vytváří zabezpečený kanál přes nezabezpečenou síť pomocí architektury klient-server. Protokol zajišťuje důvěrnost a integritu vyměňovaných dat prostřednictvím silného šifrování a kódů pro ověřování zpráv ([MAC](/mobilnisite/slovnik/mac/)). Také podporuje robustní metody ověřování, včetně kryptografie s veřejným klíčem a hesel, pro ověření identity komunikujících stran před udělením přístupu.

V kontextu 3GPP se SSH primárně používá pro zabezpečenou správu a údržbu (O&M) síťových prvků, jako jsou základnové stanice (gNB, [eNB](/mobilnisite/slovnik/enb/)), funkce jádra sítě a systémy řízení. Navázání spojení zahrnuje fázi vyjednávání, ve které se klient a server dohodnou na verzi protokolu, kryptografických algoritmech pro výměnu klíčů, symetrickém šifrování, MAC a kompresi. Následuje výměna klíčů, typicky pomocí algoritmu Diffie-Hellman, k vytvoření sdíleného tajného klíče. Tento sdílený tajný klíč se pak použije k odvození symetrických klíčů relace pro šifrování a ochranu integrity.

Architektura protokolu se skládá ze tří hlavních komponent: transportního protokolu, protokolu pro ověřování uživatele a spojovacího protokolu. Transportní vrstva zajišťuje počáteční výměnu klíčů, ověření serveru a vytvoření šifrovaného tunelu. Protokol pro ověřování uživatele spravuje ověření klienta serverem. Po ověření spojovací protokol multiplexuje šifrovaný tunel do více logických kanálů, což umožňuje interaktivní přihlašovací relace, vzdálené provádění příkazů a zabezpečený přenos souborů (pomocí [SFTP](/mobilnisite/slovnik/sftp/) nebo [SCP](/mobilnisite/slovnik/scp/)). Tato vrstvená konstrukce zajišťuje, že je zabezpečený kanál vytvořen před přenosem jakýchkoli citlivých ověřovacích údajů, a poskytuje flexibilitu pro různé typy zabezpečených datových toků.

Pro správu sítí v 3GPP je SSH specifikován v bezpečnostních a správních specifikacích (např. 33.117, 32.101) za účelem ochrany citlivých konfiguračních dat, softwarových aktualizací a výkonnostních logů před odposlechem, převzetím spojení a dalšími útoky na síťové úrovni. Jeho implementace je povinná pro zabezpečená rozhraní vzdáleného přístupu, což zajišťuje, že operátoři mohou spravovat svou distribuovanou síťovou infrastrukturu bez narušení bezpečnosti. Použití osvědčených kryptografických primitiv a obrana proti útoku typu man-in-the-middle činí z SSH základní kámen pro zabezpečený administrativní přístup v moderních telekomunikačních sítích.

## K čemu slouží

SSH byl vytvořen, aby řešil kritické bezpečnostní nedostatky starších protokolů pro vzdálené přihlašování a přenos souborů, jako jsou Telnet, rlogin a [FTP](/mobilnisite/slovnik/ftp/). Tyto starší protokoly přenášely všechna data, včetně přihlašovacích údajů (uživatelská jména a hesla), v nešifrované podobě, což je činilo vysoce zranitelnými vůči zachycení a odposlechu na nedůvěryhodných sítích. Jak se správa sítí stávala více distribuovanou a vzdálenou, riziko krádeže přihlašovacích údajů a neoprávněného přístupu výrazně rostlo.

V rámci ekosystému 3GPP potřeba SSH vyplynula z požadavku na zabezpečenou správu rozsáhlé, geograficky rozptýlené sítě skládající se z tisíců základnových stanic a uzlů jádra sítě. Tyto prvky vyžadují časté softwarové aktualizace, změny konfigurace a sledování výkonu. Použití nezabezpečených protokolů pro tyto úkoly by vystavilo celou síť manipulaci, narušení služeb a únikům dat. SSH tento problém řeší tím, že poskytuje kryptograficky zabezpečenou alternativu, která zajišťuje důvěrnost a integritu veškeré provozní komunikace.

Zavedení SSH ve standardech 3GPP, počínaje Release 8, formalizovalo dodavatelsky neutrální, interoperabilní metodu pro zabezpečenou správu a údržbu (O&M). Vyřešilo omezení proprietárních nebo slabších bezpečnostních řešení tím, že nařídilo silné, standardizované šifrování a ověřování. To bylo motivováno zejména vývojem hrozeb a regulačními požadavky na ochranu kritické telekomunikační infrastruktury. SSH umožňuje zabezpečenou automatizaci a skriptování úloh správy, což je nezbytné pro efektivní provoz rozsáhlých sítí 5G a novějších generací, aniž by se vytvořilo bezpečnostní slabé místo.

## Klíčové vlastnosti

- Silné šifrování pro důvěrnost dat pomocí algoritmů jako AES a ChaCha20
- Ochrana integrity prostřednictvím kódů pro ověřování zpráv (MAC) k zabránění manipulaci s daty
- Více metod ověřování včetně veřejného klíče, hesla a ověření na základě hostitele
- Možnosti zabezpečeného tunelování a přesměrování portů
- Vyjednávání verze protokolu a flexibilita algoritmů
- Ochrana proti útoku typu man-in-the-middle prostřednictvím ověření hostitelského klíče serveru

## Související pojmy

- [SFTP – Secure File Transfer Protocol](/mobilnisite/slovnik/sftp/)
- [TLS – Transport Layer Security](/mobilnisite/slovnik/tls/)

## Definující specifikace

- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements
- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)

---

📖 **Anglický originál a plná specifikace:** [SSH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssh/)
