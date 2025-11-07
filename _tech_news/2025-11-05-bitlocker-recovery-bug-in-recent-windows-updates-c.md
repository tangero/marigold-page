---
author: Marisa Aigen
category: kybernetická bezpečn
companies:
- Microsoft
date: '2025-11-05 16:57:00'
description: Nedávné aktualizace Windows 10 a 11 mohou na vybraných zařízeních nečekaně
  vyžadovat BitLocker recovery key; bez něj uživatel riskuje trvalou ztrátu dat. Microsoft
  problém potvrzuje a vydává opravu, komunikace však byla nedostatečná a hlavně směrem
  k firemním zákazníkům.
importance: 4
layout: tech_news_article
original_title: BitLocker recovery bug in recent Windows updates could brick your
  PC - PCWorld
publishedAt: '2025-11-05T16:57:00+00:00'
slug: bitlocker-recovery-bug-in-recent-windows-updates-c
source:
  emoji: 📰
  id: null
  name: PCWorld
title: Chyba v aktualizacích Windows vyvolává BitLocker Recovery a může zablokovat
  přístup k PC
url: https://www.pcworld.com/article/2963041/bitlocker-recovery-bug-in-recent-windows-updates-could-brick-your-pc.html
urlToImage: https://www.pcworld.com/wp-content/uploads/2025/11/preboot-pin.png?w=1024
urlToImageBackup: https://www.pcworld.com/wp-content/uploads/2025/11/preboot-pin.png?w=1024
---

## Souhrn
Nedávné aktualizace Windows vydané po 14. říjnu způsobují, že část zařízení s Windows 10 (22H2) a Windows 11 (24H2 a 25H2) náhodně naběhne do obrazovky BitLocker Recovery a vyžaduje zadání recovery key. Pokud uživatel klíč nemá zálohovaný, ztrácí přístup k systému i datům. Microsoft problém uznal, vydává opravu, ale informace byly původně viditelné hlavně pro firemní zákazníky, což zvyšuje riziko pro běžné uživatele.

## Klíčové body
- Chyba se objevuje po instalaci říjnových aktualizací Windows 10/11 a vyvolá jednorázové vyžádání BitLocker recovery key.
- Nejvíce jsou zasažena zařízení s procesory Intel podporující funkci Connected Standby (trvalé připojení v úsporném režimu).
- Bez recovery key může dojít k reálné ztrátě všech dat – BitLocker šifrování tu funguje správně, selhává proces aktualizace/bootu.
- Oprava je již distribuována, ve firemním prostředí je ale často nutné její ruční nasazení.
- Komunikace Microsoftu byla nedostatečná směrem k domácím uživatelům, přestože dopady jsou pro ně kritické.

## Podrobnosti
Podle informací z PCWorld a vyjádření Microsoftu se po instalaci vybraných aktualizací Windows vydaných po 14. říjnu objevuje scénář, kdy se systém při startu neočekávaně přepne do BitLocker Recovery. BitLocker je integrovaný nástroj pro šifrování disku ve Windows, který chrání data proti neoprávněnému přístupu. Při standardním provozu běží transparentně na pozadí a klíče jsou bezpečně uložené v TPM čipu nebo chráněny přihlašovacími údaji. Recovery key se používá pouze ve chvíli, kdy systém vyhodnotí změnu konfigurace jako rizikovou (například změna firmware, hardware, podezřelý bootovací řetězec).

Aktuální chyba způsobí, že některá zařízení, zejména s procesory Intel a podporou Connected Standby (režim, kdy notebook zůstává připojený k síti i v nízké spotřebě), jsou po aktualizaci vyhodnocena tak, že je nutné ověření přes recovery key. Microsoft uvádí, že po jednorázovém zadání správného klíče se systém chová normálně a nevyžaduje další zásahy. Problém tedy není v samotném BitLocker šifrování, ale v interakci aktualizačního procesu, správy napájení a bezpečnostních kontrol při startu.

Zásadní problém nastává u uživatelů, kteří recovery key nikdy vědomě neuložili nebo netuší, kde jej hledat. V mnoha případech je klíč při aktivaci BitLockeru automaticky uložen v Microsoft účtu, v Azure AD (u firemních zařízení) nebo v doménové infrastruktuře. Pokud ale klíč nelze dohledat, BitLocker funguje přesně podle návrhu: bez klíče k datům není přístup, což prakticky znamená jejich definitivní ztrátu. Microsoft již distribuuje opravu, ale administrační týmy ve firmách musí aktualizaci aktivně ověřit a nasadit. Kritizovat lze především to, že detailní upozornění bylo původně viditelné hlavně pro zákazníky s licencemi Microsoft 365 Business a Windows 11 Enterprise, zatímco domácí a menší uživatelé zůstali s vyšším rizikem.

## Proč je to důležité
Chyba ukazuje na strukturální problém kombinace povinných bezpečnostních mechanismů, automatizovaných aktualizací a omezené transparentnosti vůči uživatelům. BitLocker je správně navržený bezpečnostní nástroj, ale pokud aktualizace operačního systému nečekaně vyvolá recovery režim, fakticky se z bezpečnostní funkce stává potenciální příčina nedostupnosti dat.

Pro uživatele to znamená nutnost:
- okamžitě ověřit, zda mají BitLocker recovery key bezpečně uložený (Microsoft účet, firemní portál, lokální export),
- pečlivěji řídit proces aktualizací u kritických zařízení a před většími aktualizacemi provádět zálohy,
- ve firmách zajistit centrální správu klíčů a ověřit, že oprava proti tomuto problému byla nasazena na všech dotčených strojích.

Pro celý ekosystém Windows je to další signál, že kvalita testování aktualizací na kombinaci bezpečnostních funkcí (BitLocker, Secure Boot, TPM) a specifických režimů napájení musí být výrazně vyšší. Incident zároveň připomíná, že šifrování bez řádného řízení klíčů je prakticky ekvivalentní plánované ztrátě dat.

---

[Číst původní článek](https://www.pcworld.com/article/2963041/bitlocker-recovery-bug-in-recent-windows-updates-could-brick-your-pc.html)

**Zdroj:** 📰 PCWorld
